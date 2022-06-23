import requests
from decouple import config

def get_all_news():
    url=f'https://newsapi.org/v2/everything?q=money&apiKey={config("API_KEY")}'
    response=requests.get(url)
    news=response.json()
    news_list=[]
    for item in news['results']:
        if item['urlToImage'] is not None:
            news_list.append(item)
    return news_list

    