import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from newsplease import NewsPlease

subscription_key = "sy5hykat267hzj83utqa10dpxspszr4f"
assert subscription_key

def sentiment(string):
    api_url = 'https://stormy-refuge-29936.herokuapp.com/sentiment/'
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/json'
              }
    body = {
        'text': string,
    }
    response = requests.post(api_url, headers=headers, json = body)
    status = response.json()
    if response.status_code == 200:
        sentiment = status["message"]
        return sentiment
    else:
        return "Try Again Later"


# Set the URL you want to webscrape from
def scrape(string):
    url = 'https://economictimes.indiatimes.com/topic/'+string

    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    x = soup.findAll('a')
    # To download the whole data set, let's do a for loop through all a tags
    for i in range(len(x)): #'a' tags are for links
        one_a_tag = x[i]
        if one_a_tag.has_attr('href'):
            link = one_a_tag['href']
            if  not link.startswith('http'):
                if link.startswith('/markets'):
                    download_url = 'https://economictimes.indiatimes.com'+ link
                    print(download_url)
                    articles.append(NewsPlease.from_url(download_url))

    sentiments = list()

    for article in articles:
        string =  article.title + '\n' + article.text
        sentiments.append(sentiment(string))

    return sentiments
