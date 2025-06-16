# src/process_data.py
import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw_weather.csv', parse_dates=['date'])
    df = df.sort_values('date').drop_duplicates().reset_index(drop=True)
    df['temp_ma7'] = df['temp'].rolling(7, min_periods=1).mean()
    df.to_csv('data/processed_weather.csv', index=False)
    return df
