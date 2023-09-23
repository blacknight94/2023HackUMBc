'''
list of APIs
Type: Stock
	https://www.marketaux.com/account/dashboard
		Key: dhk2UcDC8sBcXYWxl3s1vakApOFz8fcPANBKuasu
Type: environmental score
	https://site.financialmodelingprep.com/developer/docs/esg-score-api/
		Key: c19ce88a3013da9410087ae6fdeed269
'''
import requests
import json
import certifi

import http.client, urllib.parse
from urllib.request import urlopen
from collections import OrderedDict

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)
# inputs are (company stock ticker)
#returns, ESG Rating: ,stock market sentiment: (Good/bad?), Price Trend: (up/down), Current Price: $ , fear and greed index: (),
def APIcalls(ticker):
    print("OUT")
    my_ordered_dict = OrderedDict()
    my_ordered_dict['name'] = 'John'
    my_ordered_dict['ticker'] = ticker

    with open('output.txt', 'w') as file:
        file.write(my_ordered_dict)
        file.write('\n')

    return my_ordered_dict

# MARKETTAUX API
"""
Relevant news:
- finance and market news
- op eds of company stocks
- 
"""
conn = http.client.HTTPSConnection('api.marketaux.com')

params = urllib.parse.urlencode({
    'api_token': 'dhk2UcDC8sBcXYWxl3s1vakApOFz8fcPANBKuasu', #The API token for connecting to the site
    'symbols': ticker, #The ticker symbols for the companies you want
    'limit': 10 , #The maximum number of articles that you want to return from the request
    'industries' : , #The type of industries you want to search for
    'countries' : , #The countries you want to search for companies in
    'sentiment_gte': , #Return articles greater than or equal to the sentiment value
    'sentiment_lte': , #Return articles less than or equal to the sentiment value
    })

conn.request('GET', '/v1/news/all?{}'.format(params))
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))


esgAPI = "c19ce88a3013da9410087ae6fdeed269"
# ESG Score info
url = "https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data?symbol=" + ticker +"&apikey="+ esgAPI
data = get_jsonparsed_data(url)
Environmental_Score = data[0].get("environmentalScore")
Social_Score = data[0].get("socialScore")
Government_Score = data[0].get("governanceScore")
Total_ESG_Score = data[0].get("ESGScore")

#esg risk rating
url = "https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data-ratings?symbol=" + ticker +"&apikey=" + esgAPI
data = get_jsonparsed_data(url)
Industries = data[0].get("industry")
ESG_Rating = data[0].get("ESGRiskRating")
Industry_Rank = data[0].get("industryRank" )

print(get_jsonparsed_data(url))
#twitter comments, and other
url  = "https://financialmodelingprep.com/api/v4/historical/social-sentiment?symbol="+ ticker +"&page=0&apikey=" + esgAPI
data = get_jsonparsed_data(url)
twitter_Posts = data[0].get("twitterPosts")
twitter_Sentiment = data[0].get("twitterSentiment")
twitter_Likes = data[0].get("twitterLikes")



