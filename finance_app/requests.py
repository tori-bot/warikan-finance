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

def youtube_trailer(title):
    search_query = title.replace(' ', '+')
    url=f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search_query}&key={config("YOUTUBE_API")}'
    response=requests.get(url)
    youtube_id = response.json()['items'][0]['id']['videoId']
    return youtube_id