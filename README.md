# WeatherTrendPredictor
A Python-based project that collects the last 3 months of weather data from an API (like OpenWeatherMap), analyzes trends (temperature, humidity, rainfall, etc.), and predicts the upcoming week's weather using approximation techniques like linear regression or ARIMA models.

# Requirements
  requests

  pandas
  
  numpy
  
  scikit-learn
  
  statsmodels
  
  python-dotenv
  
# Then install them:

bash

pip install -r requirements.txt

 #Get OpenWeatherMap API Key
Go to: https://openweathermap.org/api

Sign up and get your free API key.

Save the API key for later use.
# Create .env file
Create a file named .env inside your main folder and write:
OPENWEATHER_API_KEY=your_api_key_here
LAT=22.3569
LON=91.7832
LOCATION=Chattogram,Bangladesh

# Write Code to Fetch Weather Data
Create file: src/fetch_data.py
import os, requests, time, datetime
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

def fetch_last_90_days():
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(days=90)
    records = []

    for day in pd.date_range(start=start, end=end, freq='D'):
        ts = int(day.replace(hour=12, minute=0).timestamp())
        url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
        params = {
            "lat": LAT,
            "lon": LON,
            "dt": ts,
            "appid": API_KEY,
            "units": "metric"
        }
        res = requests.get(url, params=params)
        data = res.json()

        if 'current' in data:
            record = {
                "date": day.date(),
                "temp": data['current']['temp'],
                "humidity": data['current']['humidity'],
                "pressure": data['current']['pressure']
            }
            records.append(record)

        time.sleep(1)

    df = pd.DataFrame(records)
    df.to_csv("data/raw_weather.csv", index=False)
    return df
# Write Code to Clean Data
Create file: src/process_data.py
import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw_weather.csv', parse_dates=['date'])
    df = df.sort_values('date').drop_duplicates().reset_index(drop=True)
    df['temp_ma7'] = df['temp'].rolling(7, min_periods=1).mean()
    df.to_csv('data/processed_weather.csv', index=False)
    return df

#  Write Code to Predict Weather
Create file: src/predict_weather.py

# Write the Main Pipeline
Create the file: main.py

from src.fetch_data import fetch_last_90_days
from src.process_data import clean_data
from src.predict_weather import forecast

def run():
    print("Step 1: Fetching weather data...")
    fetch_last_90_days()

    print("Step 2: Processing data...")
    clean_data()

    print("Step 3: Predicting next 7 days temperature...")
    pred = forecast()
    print(pred)

if __name__ == "__main__":
    run()

# Run Your Project
Now just run your project from terminal:

bash
python main.py
