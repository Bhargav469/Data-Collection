# src/data_extraction.py
import requests
from bs4 import BeautifulSoup

# Extract weather data
def fetch_weather_data():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        response = requests.get(url)
        data = response.json()
        print("Weather data fetched successfully!")
        return data
    except Exception as e:
        print("Error fetching weather data:", e)
        return None

# Extract news headlines
def fetch_news_headlines():
    try:
        url = "https://opensource.com/taxonomy/term/7169/feed"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        headlines = []
        for item in items:
            headline = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            headlines.append({'headline': headline, 'url': link, 'date': pub_date})
        print("News headlines fetched successfully!")
        return headlines
    except Exception as e:
        print("Error fetching news headlines:", e)
        return []
