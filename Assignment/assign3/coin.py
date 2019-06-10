 # Calculate weignted average of coins from coinmarketcap.com

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from influxdb import InfluxDBClient

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
	'start':'1',
	'limit':'10',
	'convert':'USD'
}
headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': 'd9cada5c-a4cd-452f-bcc7-8d96559720d7',
}

session = Session()
session.headers.update(headers)
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'Market Cap Weighted Average')
client.create_database('Market Cap Weighted Average')

try:
	response = session.get(url, params=parameters)
	coin_data = json.loads(response.text)
	json_string = json.dumps( coin_data, indent =2)
	#print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)
	exit()
print()
total_market_cap=0
marketCapWeight = []
for i in range(0,10):
	total_market_cap+=int(coin_data["data"][i]["quote"]["USD"]["market_cap"])
for i in range(0,10):
	marketCapWeight.append(int(coin_data["data"][i]["quote"]["USD"]["market_cap"]) / total_market_cap)
	json_body = [
    {
        "measurement": coin_data['data'][i]['name'],

		"time": coin_data["status"]["timestamp"]  ,      
        "fields": {
            "Coin Weight": marketCapWeight[i]
        }
    }
	]
	client.write_points(json_body)

	query_string = "select * from " + coin_data['data'][0]['name'] + ';'
	ans = list(client.query(query_string))
	print(ans)

result = []
for i in range(0,10):
	str = 'hel'
# 	cpu_points = list(ans.get_points(measurement = coin_data['data'][i]['name']))
# 	json_string = json.dumps( cpu_points, indent =2)
# 	# result.append(json_string)	
print(result)
