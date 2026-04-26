import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def top_products(df):
    top = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(5)
    return top.to_dict()

def best_time(df, product):
    df_p = df[df['product'] == product]
    res = df_p.groupby('hour')['sales'].sum()
    return {"best_hour": int(res.idxmax())}

def weather_impact(df, product):
    df_p = df[df['product'] == product]
    res = df_p.groupby('weather')['sales'].mean()
    return res.to_dict()

def dynamic_price(df, product):
    avg = df[df['product'] == product]['sales'].mean()
    if avg > df['sales'].mean():
        return {"price_change": "+10% (High Demand)"}
    else:
        return {"price_change": "-5% (Low Demand)"}

def forecast(df, product):
    df_p = df[df['product'] == product]

    df_p = df_p.sort_values('datetime')
    df_p['time_index'] = np.arange(len(df_p))

    X = df_p[['time_index']]
    y = df_p['sales']

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(df_p) + i] for i in range(5)])
    preds = model.predict(future)

    return {"forecast": preds.tolist()}