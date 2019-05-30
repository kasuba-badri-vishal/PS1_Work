from influxdb import InfluxDBClient

class InfluxDbUtils:

     def get_influx_db_client(self, hostname, port, db_name, db_user, db_password):
         """Instantiate a connection to the InfluxDB."""
         return InfluxDBClient(hostname, port, db_user, db_password, db_name)

     def write_points(self, client, json_body ):
         client.write_points(json_body,time_precision='ms')