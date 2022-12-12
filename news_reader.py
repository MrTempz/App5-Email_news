import requests
import json
import os
import send_mail


news_dir = os.path.join(os.path.curdir, 'news')

api_key = 'e6138c2b6ff8420ab9ee3f5d803486dc'

def cleanup_news_dir():
    for file_name in os.listdir(news_dir):
        os.remove(os.path.join(news_dir, file_name))


def fetch_articles():
    
    with open('subscriptions.json', 'r') as f:
        subscriptions = json.load(f)
    
    topics = []
    for subscriber in subscriptions:
        topics += subscriptions[subscriber]
    topics = list(set(topics))

    cleanup_news_dir()

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

#        message = message.encode('utf-8')
        with open(os.path.join(news_dir, topic+'.txt'), 'w', encoding='utf-8') as f:
            f.write(message)

if __name__ == '__main__':
    fetch_articles()
    with open('subscriptions.json', 'r') as f:
        subscriptions = json.load(f)
    
    message = "Subject: Today's news \n"
    for subscriber in subscriptions:
        if subscriber == 'adamtemplin92@gmail.com':
            topics = subscriptions[subscriber]
            for topic in topics:
                with open(os.path.join(news_dir, topic+'.txt'), 'r', encoding='utf-8') as f:
                    message += topic.title() + '\n' + f.read()
            message = message.encode('utf-8')
            send_mail.send_email(message=message)


