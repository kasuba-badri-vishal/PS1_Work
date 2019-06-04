# import requests

# resp = requests.get('https://cointelegraph.com')
# resp1 = requests.get('https://cointelegraph.com/news/bitcoins-overnight-crash-doesnt-stop-experts-from-remaining-macro-bullish')
# resp2 = requests.get('https://api-pub.bitfinex.com/v2/stats1/credits.size:1m:fUSD/last')
# print(resp.status_code)
# print(resp1.status_code)

import requests

shots_url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
    'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
    'PlayerID=202322&Season=2014-15&SeasonSegment=&' + \
    'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='

# request the URL and parse the JSON
response = requests.get(shots_url)
response.raise_for_status() # raise exception if invalid response
shots = response.json()['resultSets'][0]['rowSet']

# do whatever we want with the shots data
do_things(shots)