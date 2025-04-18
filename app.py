import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error

# --- Page Configuration ---
st.set_page_config(
    page_title="Enterprise Time Series Forecaster",
    layout="wide",
    page_icon="📈"
)

# --- App Header ---
st.title("📊 Agentic AI Powered Time Series Forecasting")
st.markdown("An intelligent forecasting dashboard powered by modular agents and Prophet.")
st.markdown("---")

# --- Sidebar Settings ---
st.sidebar.header("📂 Configuration")
data_path = "daily_sales.csv"
forecast_path = "forecast.csv"

# --- Load Data ---
@st.cache_data
def load_data():
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        df['ds'] = pd.to_datetime(df['ds'])
        return df
    return pd.DataFrame()

@st.cache_data
def load_forecast():
    if os.path.exists(forecast_path):
        df = pd.read_csv(forecast_path)
        df['ds'] = pd.to_datetime(df['ds'])
        return df
    return pd.DataFrame()

df = load_data()
forecast_df = load_forecast()

if df.empty or forecast_df.empty:
    st.error("❌ Required data not found. Please run the pipeline first.")
    st.stop()

# --- Metric Comparison ---
st.subheader("📉 Key Forecast Metrics")
actual = df['y'].values[-60:]
forecast = forecast_df['yhat'].values[-60:]

if len(actual) == len(forecast):
    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(mean_squared_error(actual, forecast))
    mape = np.mean(np.abs((actual - forecast) / actual)) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("MAE", f"{mae:.2f}")
    col2.metric("RMSE", f"{rmse:.2f}")
    col3.metric("MAPE", f"{mape:.2f}%")
else:
    st.warning("⚠️ Could not calculate error metrics — mismatch in actual vs forecast data length.")

# --- Interactive Forecast Plot ---
st.subheader("📈 Forecast Chart")
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['ds'], y=df['y'], mode='lines', name='Actual Sales',
    line=dict(color='royalblue')
))

fig.add_trace(go.Scatter(
    x=forecast_df['ds'], y=forecast_df['yhat'], mode='lines', name='Forecast',
    line=dict(color='orange', dash='dash')
))

fig.update_layout(
    height=500,
    margin=dict(l=30, r=30, t=30, b=30),
    xaxis_title="Date",
    yaxis_title="Sales",
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# --- Expandable Raw Data Section ---
with st.expander("🧾 View Raw Input Data"):
    st.dataframe(df.tail(10), use_container_width=True)

with st.expander("🔮 View Forecast Output (Next 60 Days)"):
    st.dataframe(forecast_df.tail(60).reset_index(drop=True), use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown(
    "🚀 Built by **Mrig Debsarma** | "
    "Powered by **LangChain-style Agents**, **Prophet**, and **Streamlit**"
)
