# Day 30

import requests

api_key = "3e55716c908c4e1d85ead75f68be3390"
url = ("https://newsapi.org/v2/everything?q="
       "tesla&from=2024-02-23&sortBy=publishedAt&apiKey="
       "3e55716c908c4e1d85ead75f68be3390")

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
