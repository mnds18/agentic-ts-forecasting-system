"""
Agentic AI Time Series Forecasting System
Full Pipeline Orchestrator with Modular Agents and Live API
"""

import time
from flask import Flask, jsonify
from agents.requirements_agent import run_requirements_gathering
from agents.data_generation_agent import run_data_generation
from agents.data_scientist_agent import run_model_training
from agents.peer_review_agent import run_peer_review
from agents.documentation_agent import generate_report
from agents.project_manager_agent import generate_plan_and_gantt
from agents.presentation_agent import generate_slide_deck
from agents.orchestration_agent import log_event

# Step tracker for orchestration log
orchestration_log = []

# Initialize Flask API
app = Flask(__name__)

@app.route("/forecast", methods=["GET"])
def serve_forecast():
    import pandas as pd
    forecast_path = "data/forecast.csv"
    if not os.path.exists(forecast_path):
        return jsonify({"error": "Forecast not found. Run pipeline first."}), 404
    df = pd.read_csv(forecast_path).tail(60)
    return jsonify(df.to_dict(orient="records"))

# Orchestration wrapper

def run_pipeline():
    steps = [
        ("Business Analyst", run_requirements_gathering),
        ("Data Generator", run_data_generation),
        ("Data Scientist", run_model_training),
        ("Peer Reviewer", run_peer_review),
        ("Documentation Generator", generate_report),
        ("Project Manager", generate_plan_and_gantt),
        ("Presentation Agent", generate_slide_deck),
    ]

    print("\n🚀 Starting Agentic Time Series Forecasting Workflow")
    for step_name, step_fn in steps:
        start = time.time()
        print(f"\n🔹 Running: {step_name} Agent")
        output = step_fn()
        end = time.time()

        log_event(
            agent_name=step_name,
            step=step_fn.__name__,
            start_time=start,
            end_time=end,
            output_summary=str(output)[:150] + ("..." if len(str(output)) > 150 else "")
        )

    print("\n✅ All agents completed successfully.")
    print("📈 Forecast ready. Report, slides, Gantt chart, and peer review are available in the outputs/ folder.")
    print("🌐 API available at http://localhost:5001/forecast")


if __name__ == "__main__":
    run_pipeline()
    app.run(port=5001)
