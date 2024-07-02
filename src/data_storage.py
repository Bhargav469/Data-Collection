# src/data_storage.py
from config.db_config import get_db_connection
import pandas as pd

def store_weather_data(df):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO weather_data (time, temperature, humidity, wind_speed) VALUES (%s, %s, %s, %s)",
                (row['time'], row['temperature'], row['humidity'], row['wind_speed'])
            )
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Weather data stored successfully!")
    except Exception as e:
        print("Error storing weather data:", e)

def store_news_headlines(df):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO web_headlines (headline, url, date) VALUES (%s, %s, %s)",
                (row['headline'], row['url'], row['date'])
            )
        
        conn.commit()
        cursor.close()
        conn.close()
        print("News headlines stored successfully!")
    except Exception as e:
        print("Error storing news headlines:", e)
