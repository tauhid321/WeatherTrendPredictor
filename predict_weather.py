# src/predict_weather.py
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast(days=7):
    df = pd.read_csv('data/processed_weather.csv', parse_dates=['date']).set_index('date')
    model = ARIMA(df['temp_ma7'], order=(2,1,2)).fit()
    pred = model.forecast(days)
    return pred
