import requests
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost',port=8086)

print(client)
client.create_database('badri_db')
# client.switch_database('learn_db')
resp = requests.get('https://api-pub.bitfinex.com/v2/stats1/funding.size:1m:fUSD/last')
resp2 = requests.get('https://api-pub.bitfinex.com/v2/stats1/credits.size:1m:fUSD/last')

if resp.status_code == 200:
    print("working")
    print(resp)
    print(resp.status_code)
    print(resp.content)
else :
    print("not Working")

if resp2.status_code == 200:
    print("working")
    print(resp2)
    print(resp2.status_code)
    print(resp2.content)
else :
    print("not Working")

# client.write_points(resp.json())

    
    