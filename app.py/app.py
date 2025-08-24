from src.weather import get_weather
from src.news import get_headlines

if __name__ == "__main__":
    city = "New York"
    weather = get_weather(city)
    news = get_headlines()

    print(f"🌤️ Weather in {city}: {weather['temperature']}°C, {weather['description']}")
    print("\n📰 Top News Headlines:")
    for i, headline in enumerate(news, 1):
        print(f"{i}. {headline}")
