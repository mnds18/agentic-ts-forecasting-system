"""
data_generation_agent.py
Data Generator Agent to simulate 3 years of daily data with COVID-like black swan
"""

import pandas as pd
import numpy as np
import os

def run_data_generation():
    dates = pd.date_range(start="2020-01-01", end="2022-12-31")
    np.random.seed(42)
    trend = np.linspace(100, 600, len(dates))
    seasonal = 50 * np.sin(np.linspace(0, 3 * np.pi, len(dates)))
    noise = np.random.normal(0, 25, len(dates))
    black_swan = np.where((dates >= "2020-03-15") & (dates <= "2020-06-15"), -150, 0)
    sales = trend + seasonal + noise + black_swan
    df = pd.DataFrame({"ds": dates, "y": sales})
    df.to_csv("data/daily_sales.csv", index=False)
    return df