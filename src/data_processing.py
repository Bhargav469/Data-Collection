# src/data_processing.py
import pandas as pd

# Process weather data
def process_weather_data(data):
    try:
        hourly_data = data['hourly']
        timestamps = hourly_data['time']
        temperatures = hourly_data['temperature_2m']
        humidities = hourly_data['relative_humidity_2m']
        wind_speeds = hourly_data['wind_speed_10m']
        
        # Data cleansing: Handling missing values by filling with the mean
        temperatures = [t if pd.notna(t) else temperatures.mean() for t in temperatures]
        humidities = [h if pd.notna(h) else humidities.mean() for h in humidities]
        wind_speeds = [w if pd.notna(w) else wind_speeds.mean() for w in wind_speeds]
        
        weather_df = pd.DataFrame({
            'time': timestamps,
            'temperature': temperatures,
            'humidity': humidities,
            'wind_speed': wind_speeds
        })
        print("Weather data processed successfully!")
        return weather_df
    except Exception as e:
        print("Error processing weather data:", e)
        return None

# Process news headlines
def process_news_headlines(headlines):
    try:
        headlines_df = pd.DataFrame(headlines)
        
        # Data cleansing: Removing duplicate headlines
        headlines_df.drop_duplicates(subset=['headline'], keep='first', inplace=True)
        
        print("News headlines processed successfully!")
        return headlines_df
    except Exception as e:
        print("Error processing news headlines:", e)
        return None
