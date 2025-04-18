```
# Agentic AI Time Series Forecasting System - Wiki

## System Overview
An end-to-end enterprise-grade pipeline demonstrating the application of Agentic AI to time series forecasting using modular agents.

## Architecture
- **Business Analyst Agent**: Gathers requirements
- **Data Generator Agent**: Produces 3 years of synthetic daily data with black swan scenarios
- **Data Scientist Agent**: Builds multiple forecasting models (Prophet, ARIMA, XGBoost)
- **Peer Review Agent**: Audits code for reproducibility, modularity, testing
- **MLOps Agent**: Deploys forecast via Flask API
- **PM Agent**: Generates project plan and visual Gantt
- **Documentation Agent**: Creates reports, metrics, and summaries
- **Presentation Agent**: Builds exec/technical slides
- **Orchestration Agent**: Logs and tracks each agent's execution and duration

## Tech Stack
- Python, Streamlit, Plotly, Pandas, Prophet, ARIMA, XGBoost
- Flask API for inference endpoint
- Modular agents inspired by LangGraph

## Execution Flow
Each agent takes input from the previous, performs its role, and passes output forward.

## Deployment Options
- Local execution via CLI
- Interactive demo via Streamlit
- Docker container available
```