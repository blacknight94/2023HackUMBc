'''
list of APIs
Type: Stock
	https://www.marketaux.com/account/dashboard
		Key: dhk2UcDC8sBcXYWxl3s1vakApOFz8fcPANBKuasu
Type: environmental score
	https://site.financialmodelingprep.com/developer/docs/esg-score-api/
		Key: c19ce88a3013da9410087ae6fdeed269
'''
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
def esgAPITwo(ticker):
    my_ordered_dict = OrderedDict()
    my_ordered_dict['name'] = 'John'
    my_ordered_dict['ticker'] = ticker
    esgAPI = "c19ce88a3013da9410087ae6fdeed269"
    # ESG Score info
    """
    url = "https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data?symbol=" + ticker + "&apikey=" + esgAPI
    data = get_jsonparsed_data(url)
    my_ordered_dict["Environmental_Score"] = data[0].get("environmentalScore")
    my_ordered_dict["Social_Score"] = data[0].get("socialScore")
    my_ordered_dict["Government_Score"] = data[0].get("governanceScore")
    my_ordered_dict["Total_ESG_Score"] = data[0].get("ESGScore")

    # esg risk rating
    url = "https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data-ratings?symbol=" + ticker + "&apikey=" + esgAPI
    data = get_jsonparsed_data(url)
    my_ordered_dict["Industries"] = data[0].get("industry")
    my_ordered_dict["ESG_Rating"] = data[0].get("ESGRiskRating")
    my_ordered_dict["Industry_Rank"] = data[0].get("industryRank")

    print(get_jsonparsed_data(url))
    # twitter comments, and other
    url = "https://financialmodelingprep.com/api/v4/historical/social-sentiment?symbol=" + ticker + "&page=0&apikey=" + esgAPI
    data = get_jsonparsed_data(url)
    my_ordered_dict["twitter_Posts"] = data[0].get("twitterPosts")
    my_ordered_dict["twitter_Sentiment"] = data[0].get("twitterSentiment")
    my_ordered_dict["twitter_Likes"] = data[0].get("twitterLikes")
    """
    my_ordered_dict["Environmental_Score"] = "38.5"
    my_ordered_dict["Social_Score"] = "2.13"
    my_ordered_dict["Total_ESG_Score"] = "37"
    my_ordered_dict["Industries"] = "Maufacturing, Electical, Software"
    my_ordered_dict["ESG_Rating"] = "84.7"
    my_ordered_dict["Industry_Rank"] = "B+" 
    my_ordered_dict["twitter_Posts"] = "3562"
    my_ordered_dict["twitter_Sentiment"] = "36.6"
    my_ordered_dict["twitter_Likes"] = "23578"

    with open('output.txt', 'w') as file:
        for key, value in my_ordered_dict:
            file.write(f'{key}: {value},')
        file.write('\n')

    return my_ordered_dict
