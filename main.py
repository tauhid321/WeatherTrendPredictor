from src.fetch_data import fetch_last_90_days
from src.process_data import clean_data
from src.predict_weather import forecast

def run():
    print("Fetching data...")
    fetch_last_90_days()

    print("Processing data...")
    clean_data()

    print("Forecasting next 7 days (temperature)...")
    pred = forecast()
    print(pred)

if __name__ == "__main__":
    run()
