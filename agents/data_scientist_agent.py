"""
data_scientist_agent.py
Data Scientist Agent to train and compare multiple forecasting models
"""

import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import os


def run_model_training():
    df = pd.read_csv("data/daily_sales.csv")
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.sort_values("ds")

    train = df[:-60]
    test = df[-60:]

    # Train Prophet
    model = Prophet()
    model.fit(train)
    future = model.make_future_dataframe(periods=60)
    forecast = model.predict(future)

    forecast["y_true"] = list(train["y"]) + list(test["y"])
    forecast["split"] = ["train"] * len(train) + ["test"] * 60
    forecast.to_csv("data/forecast.csv", index=False)

    # Calculate error metrics
    y_true = test["y"].values
    y_pred = forecast["yhat"].values[-60:]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    metrics = pd.DataFrame.from_dict({
        "Model": ["Prophet"],
        "MAE": [mae],
        "RMSE": [rmse],
        "MAPE": [mape]
    })
    metrics.to_csv("outputs/model_report.csv", index=False)

    return metrics
