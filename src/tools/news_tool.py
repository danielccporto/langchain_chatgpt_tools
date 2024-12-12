import requests
from src.utils.api_keys import NEWS_API_KEY

def get_news(topic: str) -> str:
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            top_article = articles[0]
            return f"Notícia: {top_article['title']} - {top_article['description']} (Fonte: {top_article['source']['name']})."
    return "Não foi possível encontrar notícias sobre esse tópico."
