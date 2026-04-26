import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Extract useful features
    df['hour'] = df['datetime'].dt.hour
    df['day'] = df['datetime'].dt.day_name()
    df['month'] = df['datetime'].dt.month

    return df