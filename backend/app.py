from flask import Flask, request, jsonify
import pandas as pd
from model import best_time, top_products, forecast

app = Flask(__name__)

df = pd.read_csv("data/coffee_sales.csv")

@app.route("/best-time", methods=["GET"])
def best_time():
    item = request.args.get("item")
    result = best_time(df, item)
    return jsonify(result)

@app.route("/top-products", methods=["GET"])
def top():
    result = top_products(df)
    return jsonify(result)

@app.route("/predict", methods=["GET"])
def predict():
    item = request.args.get("item")
    weather = request.args.get("weather")
    result = forecast(df, item, weather)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)