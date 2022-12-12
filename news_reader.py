import requests
import json

api_key = 'e6138c2b6ff8420ab9ee3f5d803486dc'

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-11-12&" \
    "sortBy=publishedAt&apiKey=e6138c2b6ff8420ab9ee3f5d803486dc"

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])