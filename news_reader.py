import requests
import json
import os
import send_mail


news_dir = os.path.join(os.path.curdir, 'news')

api_key = 'e6138c2b6ff8420ab9ee3f5d803486dc'

articles = {}

def fetch_articles():
    with open('subscriptions.json', 'r') as f:
        subscriptions = json.load(f)
    
    topics = []
    for subscriber in subscriptions:
        topics += subscriptions[subscriber]
    topics = list(set(topics))

    for topic in topics:
        url = f'https://newsapi.org/v2/everything?q={topic}&from=2022-11-12&' \
        'sortBy=publishedAt&apiKey=e6138c2b6ff8420ab9ee3f5d803486dc&language=en'
        request = requests.get(url)
        content = request.json()

        message = ''
        for article in content['articles'][:20]:
            if article['title']:
                message += '\t' + article['title'] + '\n'
                message += '\t' + article['description'] + '\n'
                message += article['url'] + '\n'*3
        message = message.encode('utf-8')
        articles[topic.replace(' ', '_')] = message

def compose_email(user_email):
    with open('subscriptions.json', 'r') as f:
        subscriptions = json.load(f)
    if (user_email in subscriptions.keys()):
        topics = subscriptions[user_email]
        message = "Subject: Today's news \n\n"
        message = message.encode('utf-8')
        for topic in topics:
            message += articles[topic.replace(' ', '_')]
        return message

if __name__ == '__main__':
    fetch_articles()
    with open('subscriptions.json', 'r') as f:
        subscriptions = json.load(f)
    
    fetch_articles()
    message = compose_email('adamtemplin92@gmail.com')
    send_mail.send_email(message=message)
