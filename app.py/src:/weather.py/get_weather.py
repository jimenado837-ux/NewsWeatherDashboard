import requests

def get_weather(city: str):
    api_key = "YOUR_API_KEY"  # from OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except (requests.RequestException, KeyError, IndexError):
        return {
            "city": city,
            "temperature": None,
            "description": "Weather data unavailable"
        }
