'''
list of APIs
Type: Stock
    https://www.marketaux.com/account/dashboard
        Key: dhk2UcDC8sBcXYWxl3s1vakApOFz8fcPANBKuasu
Type: environmental score
    https://site.financialmodelingprep.com/developer/docs/esg-score-api/
        Key: c19ce88a3013da9410087ae6fdeed269
Type: media sentiment
    https://www.marketaux.com/
        Key: NsdaXCKVAUHOUJ6LqZp38DfFLfWUU2vPn3nDszKP
'''
# Imports
import json
import certifi

import http.client, urllib.parse
from urllib.request import urlopen
from collections import OrderedDict

import numpy as np

sentimentList = []

# Checks if the company ticker is mentioned in the article and returns the entity index for which the company ticker was found
# If the company is not mentioned, doesn't return anything
def checkCompanyMention(companyTicker, article):
    mentions = article['entities']
    entityIndex = 0
    mentionFound = False
    for mention in mentions:
        if companyTicker == mention['symbol']:
            mentionFound = True
            return entityIndex
        else:
            entityIndex += 1
    if mentionFound != True:
        return None


# Accesses the specific entity found from the checkCompanyMention, extracts the sentiment score, and adds it to the sentiment score list
def addSentimentScore(article, entityIndex):
    sentimentList.append(article['entities'][entityIndex]['sentiment_score'])


# Turns the list of sentiment scores into an array and calculates the average using NumPy
def calculateAverageSentiment(allSentiments):
    averageSentiment = np.mean(np.array(allSentiments))
    return averageSentiment


# Gathers the article properties for which the company was mentioned such as title, url, snippet, and publishing datetime
def gatherArticleProperties(article):
    title = article['title']
    url = article['url']
    snippet = article['snippet']
    publishing = article['published_at']
    return title, url, snippet, publishing


# inputs are (company stock ticker)
# returns, ESG Rating: ,stock market sentiment: (Good/bad?), Price Trend: (up/down), Current Price: $ , fear and greed index: (),

# Templating code
    # Cole
    # MarketTauxAPI Call, creates dataset containing all the articles returned by the search pertaining to a company of interest

    # Driver code
    # 1. Take the first company ticker
    # 2. Check each of the articles to see if the company is mentioned
    # 3. If the company is mentioned, get the sentiment score and add it to the array of sentiments. In addition, gather the
    # article properties
    # 4. Add the all the articles and their properties to th e company's list of articles
    # 5. Calculate the company's average sentiment and add the score to the company's average sentiment
    # 6. Add the company name to the name field
    # 7. Move to the next company ticker and repeat steps 1-6 until all the companies have been accounted for
def newsAPICall(ticker):
    ticker = ticker.upper()
    conn = http.client.HTTPSConnection('api.marketaux.com')
    params = urllib.parse.urlencode({
       'api_token': 'NsdaXCKVAUHOUJ6LqZp38DfFLfWUU2vPn3nDszKP',
       'symbols': ticker,
       'limit': 3,
       'must_have_entities': True
    })
    conn.request('GET', '/v1/news/all?{}'.format(params))
    res = conn.getresponse()

    data = res.read()
    dataset = json.loads(data.decode('utf-8'))
    companies = [ticker]
    companySentiments = {
       company: {
          'name': '',
          'average sentiment': float,
          'articles': []
       }
       for company in companies
    }
    for company in companies:  # Step 1
        for newsArticle in dataset['data']:  # Step 2
            entityInd = checkCompanyMention(company, newsArticle)
            if entityInd != None:  # Step 3
                addSentimentScore(newsArticle, entityInd)
                title, url, snippet, publishing = gatherArticleProperties(newsArticle)
                companySentiments[company]['articles'].append(
                    {'title': title, 'url': url, 'snippet': snippet, 'published_at': publishing})  # Step 4
            companySentiments[company]['average sentiment'] = calculateAverageSentiment(sentimentList)  # Step 5
            companySentiments[company]['name'] = newsArticle['entities'][entityInd]['name']  # Step 6
    print(companySentiments)
    return companySentiments

