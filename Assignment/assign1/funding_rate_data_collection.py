import os
import json
import urllib
import requests
import logging
import sys
from time import sleep
# from historical_data.influx_db_utilities import InfluxDbUtils

class FundingRateHistoricalData:
    def __init__(self):
        self.db_user = os.getenv("DB_USERNAME")
        logfile = os.getenv('LOG_FILE')
        self.setup_logger(logfile)
        self.port = os.getenv("INFLUX_DB_PORT")
        self.db_password = os.getenv("DB_PASSWORD")
        self.hostname = os.getenv("INFLUX_DB_HOSTNAME")
        self.polling_frequency = os.getenv("POLLING_FREQUENCY")
        self.historical_data_db_name = os.getenv("HISTORICAL_DATA_DB_NAME")
        self.funding_rate_exchanges_data_file_name = os.getenv("EXCHANGES_DATA_FILE_NAME")
        self.exchanges_data_json = self.get_exchanges_data(self.funding_rate_exchanges_data_file_name)
        self.bitmex_deribit_data_measurement_name = os.getenv("FUNDING_RATE_DATA_MEASUREMENT_NAME")

    def setup_logger(self, logfile):
        if hasattr(self, 'logger'):
            getattr(self, 'logger').handlers = []
        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler(logfile, mode='a')
        handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.addHandler(screen_handler)

    def run_loop(self):
        while True:
            historical_data = []
            for exchange in self.exchanges_data_json:
                exchange_name = exchange["exchange_name"]
                exchange_api = exchange["instrument_funding_rate_data_api"]
                exchange_instrument_list = self.get_instrument_list(exchange)
                for instrument in exchange_instrument_list:
                    try:
                        instrument_data_json = self.get_historical_data(exchange_name, exchange_api, instrument)
                        funding_rate_data = self.get_funding_rate_data(instrument_data_json, exchange)
                        funding_rate_data_8h = self.get_funding_rate_data_8h(instrument_data_json, exchange)
                        influxdb_data_obj = FundingRateHistoricalDataInfluxDB(exchange_name, instrument, funding_rate_data, funding_rate_data_8h)
                        json_body = self.get_influxdb_query_json_body(self.bitmex_deribit_data_measurement_name, influxdb_data_obj)
                        historical_data.append(json_body)
                    except Exception as e:
                        self.logger.info("Exception caught while fetching data through Rest Call" + str(e))
            influx_db_client = InfluxDbUtils().get_influx_db_client(self.hostname, self.port, self.historical_data_db_name, self.db_user, self.db_password)
            try:
                self.logger.info("Writing points to Influx DB: " + self.historical_data_db_name)
                if historical_data:
                    self.logger.info("Data to be written in influx db: " + str(historical_data))
                    self.write_points_influx_db(influx_db_client, historical_data)
                else:
                    self.logger.info("No data available for writing.Hence skipping.")
            except Exception as e:
                self.logger.info("Exception encountered while writing points to Influx DB: " + str(e))
            sleep(int(self.polling_frequency))

    def write_points_influx_db(self, client, json_body):
        retry_count = 3
        count = 0
        while count < retry_count:
            count = count + 1
            try:
                InfluxDbUtils().write_points(client, json_body)
                break
            except Exception as e:
                self.logger.info("Exception encountred while writing to Influx DB: " + str(e))
                continue

    def get_exchanges_data(self,file_name):
        with open(file_name, 'r') as f:
            exchanges_data = json.load(f)
        return exchanges_data["exchanges"]

    def get_instrument_list(self, exchange_data):
        return exchange_data["instruments"].split(",")

    def get_historical_data(self, exchange_name, exchange_data_api, instrument_name ):
        api_url = exchange_data_api.replace("<instrument_name>", instrument_name)
        if exchange_name == "Bitmex":
            data = self.get_bitmex_historical_data(api_url)
            return data
        if exchange_name == "Deribit":
            data = self.get_deribit_historical_data(api_url)
            return data
        if exchange_name == "GateIO":
            data = self.get_gateio_historical_data(api_url)
            return data

    def get_funding_rate_data(self, instrument_data_json, exchanges_data_json):
        return instrument_data_json[exchanges_data_json['funding_rate_data_key_name']]

    def get_funding_rate_data_8h(self, instrument_data_json, exchanges_data_json):
        return instrument_data_json[exchanges_data_json['funding_rate_data_8h_key_name']]

    def get_bitmex_historical_data(self, api_url):
        self.logger.info(api_url)
        try:
            api_response= requests.get(api_url)
        except urllib.error.URLError as e:
            self.logger.info("Exception occured while fetching the url:" +str(e))
        finally:
            return json.loads(json.dumps(api_response.json()[0]))

    def get_deribit_historical_data(self, api_url):
        self.logger.info(api_url)
        try:
            api_response = requests.get(api_url)
        except urllib.error.URLError as e:
            self.logger.info("Exception occureed while fetching the url:" + str(e))
        finally:
            return json.loads(json.dumps(api_response.json()["result"]))

    def get_gateio_historical_data(self, api_url):
        self.logger.info(api_url)
        try:
            api_response = requests.get(api_url)
        except urllib.error.URLError as e:
            self.logger.info("Exception occureed while fetching the url:" + str(e))
        finally:
            return json.loads(json.dumps(api_response.json()[0]))

    def get_influxdb_query_json_body(self, measurement, db_data_object):
        json_body = {}
        json_body['tags'] = {}
        json_body['fields'] = {}
        json_body["measurement"] = measurement
        json_body["tags"]["exchange"] = db_data_object.get_exchange_name()
        json_body["tags"]["instrument"] = db_data_object.get_instrument()
        json_body["fields"]["funding_rate"] = db_data_object.get_funding_rate()
        json_body["fields"]["funding_rate_8h"] = db_data_object.get_funding_rate_8h()
        return json_body

class FundingRateHistoricalDataInfluxDB:
     def __init__(self, exchane_name, instrument, fundingrate,fundingrate8h ):
         self.funding_rate = float(fundingrate)
         self.funding_rate_8h = float(fundingrate8h)
         self.instrument = instrument
         self.exchange_name = exchane_name

     def get_exchange_name(self):
         return self.exchange_name

     def get_instrument(self):
         return self.instrument

     def get_funding_rate(self):
         return self.funding_rate

     def get_funding_rate_8h(self):
         return self.funding_rate_8h