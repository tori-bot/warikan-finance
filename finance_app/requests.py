import requests
from decouple import config

def get_all_news():
    url=f'https://newsapi.org/v2/everything?q=money&apiKey={config("API_KEY")}'
    response=requests.get(url)
    news=response.json()
    news_list=[]
    for item in news['articles']:
        if item['urlToImage'] is not None:
            news_list.append(item)
    return news_list

def youtube_videos():
    title='money management'
    search_query = title.replace(' ', '+')
    url=f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={search_query}&key={config("YOUTUBE_API")}'
    response=requests.get(url)
    videos = response.json()
    video_list=[]
    for item in videos['items']:
        if item['id']['videoId'] is not None:
            videoId=item['id']['videoId']
            trailer_url=f'https://www.youtube.com/embed/{videoId}?autoplay=0&muted=1'
            video_list.append(trailer_url)
    return video_list