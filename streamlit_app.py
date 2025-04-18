import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from math import sqrt

st.set_page_config(page_title="Agentic Forecasting Dashboard", layout="wide", page_icon="📊")

st.title("📊 Agentic Time Series Forecasting Dashboard, by Mrig")
st.markdown("Built with modular agents: BA → DS → Reviewer → MLOps → PM")

# Load Data
data_path = "data/daily_sales.csv"
forecast_path = "data/forecast.csv"
log_path = "outputs/orchestration_log.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(data_path)
    df['ds'] = pd.to_datetime(df['ds'])
    return df

@st.cache_data
def load_forecast():
    df = pd.read_csv(forecast_path)
    df['ds'] = pd.to_datetime(df['ds'])
    return df

@st.cache_data
def load_log():
    df = pd.read_csv(log_path)
    df['Start Time'] = pd.to_datetime(df['Start Time'], unit='s')
    df['End Time'] = pd.to_datetime(df['End Time'], unit='s')
    return df

sales_df = load_data()
forecast_df = load_forecast()
log_df = load_log()

# Section 1: Forecast Chart
st.subheader("📈 Forecast vs Actual")
fig = go.Figure()
fig.add_trace(go.Scatter(x=sales_df['ds'], y=sales_df['y'], mode='lines', name='Actual'))
fig.add_trace(go.Scatter(x=forecast_df['ds'], y=forecast_df['yhat'], mode='lines', name='Forecast'))
fig.update_layout(title="Retail Sales Forecast", xaxis_title="Date", yaxis_title="Sales", height=450)
st.plotly_chart(fig, use_container_width=True)

# Section 2: Forecast Metrics
st.subheader("📊 Forecast Metrics")
common_dates = set(sales_df['ds']).intersection(set(forecast_df['ds']))
actual = sales_df[sales_df['ds'].isin(common_dates)].sort_values('ds')['y']
pred = forecast_df[forecast_df['ds'].isin(common_dates)].sort_values('ds')['yhat']

if not actual.empty and not pred.empty:
    mae = mean_absolute_error(actual, pred)
    rmse = sqrt(mean_squared_error(actual, pred))
    mape = np.mean(np.abs((actual - pred) / actual)) * 100
    col1, col2, col3 = st.columns(3)
    col1.metric("MAE", f"{mae:.2f}")
    col2.metric("RMSE", f"{rmse:.2f}")
    col3.metric("MAPE", f"{mape:.2f}%")
else:
    st.warning("Forecast and actual overlap insufficient for metric calculation.")

# Section 3: Agent Execution Log
st.subheader("🧾 Agent Execution Log")
st.dataframe(log_df, use_container_width=True)

# Section 4: Raw Data Tabs
with st.expander("📄 Raw Data View"):
    tab1, tab2 = st.tabs(["Actual Sales", "Forecast"])
    tab1.dataframe(sales_df.tail(10), use_container_width=True)
    tab2.dataframe(forecast_df.tail(10), use_container_width=True)

st.markdown("---")
st.caption("Built by Mrig Debsarma | Powered by Agentic AI, Streamlit, and Plotly")
