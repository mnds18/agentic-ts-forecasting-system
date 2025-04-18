"""
requirements_agent.py
Business Analyst Agent to gather requirements and output project summary
"""

import json
import os

def run_requirements_gathering():
    result = {
        "business_type": "Retail Sales",
        "forecast_horizon": "60 days",
        "granularity": "Daily",
        "critical_periods": ["End of Year", "Promotions"],
        "success_metric": "MAPE < 10%",
        "volatility_events": ["COVID dip"]
    }
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/requirements_summary.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
    return result