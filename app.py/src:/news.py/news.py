import requests

def get_headlines():
    api_key = "YOUR_NEWS_API_KEY"  # from NewsAPI.org
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()["articles"]
    return [a["title"] for a in articles[:5]]
