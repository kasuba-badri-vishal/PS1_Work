import requests

url = ('https://cointelegraph.com/tags/india?''apikey=0b4f45e8bb1d4290a227d575a44bedbb')
response = requests.get(url)
print(response.status_code)




# import requests
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=in&'
#        'apiKey=0b4f45e8bb1d4290a227d575a44bedbb')

# url = 
# response = requests.get(url)
# print(response.json())


# import requests
# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=crypto-coins-news&'
#        'apiKey=0b4f45e8bb1d4290a227d575a44bedbb')\
# url = ('https://newsapi.org/v2/everything?'
#        'q=Bitcoin&'
#        'from=2019-30-03&'
#        'country=in&'
#        'sortBy=popularity&'
#        'apiKey=0b4f45e8bb1d4290a227d575a44bedbb')


# url = ('https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&country=in&apiKey=0b4f45e8bb1d4290a227d575a44bedbb')
# response = requests.get(url)
# print(response.json())


# from newsapi import NewsApiClient

# newsapi = NewsApiClient(api_key = '0b4f45e8bb1d4290a227d575a44bedbb')

# top_headlines = newsapi.get_top_headlines(q='bitcoin', category='business',language='en',country='in')
# print(top_headlines)