# src/main.py
from src.data_extraction import fetch_weather_data, fetch_news_headlines
from src.data_processing import process_weather_data, process_news_headlines
from src.data_storage import store_weather_data, store_news_headlines

def main():
    # Fetch data
    weather_data = fetch_weather_data()
    news_headlines = fetch_news_headlines()
    
    # Process data
    weather_df = process_weather_data(weather_data)
    news_df = process_news_headlines(news_headlines)
    
    # Store data
    store_weather_data(weather_df)
    store_news_headlines(news_df)

if __name__ == "__main__":
    main()
