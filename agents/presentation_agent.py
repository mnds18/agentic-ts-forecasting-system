"""
presentation_agent.py
Creates slide_deck.md with content for both execs and technical teams
"""

def generate_slide_deck():
    slides = {
        "Slide 1": "Objective: Forecast retail sales using modular agentic pipeline",
        "Slide 2": "Architecture: BA → DS → Reviewer → MLOps → PM",
        "Slide 3": "Models: Prophet baseline + XGBoost/ARIMA planned",
        "Slide 4": "Data: 3 years daily + black swan (COVID dip)",
        "Slide 5": "Forecast Output: CSV + API + Dashboard",
        "Slide 6": "Key Metrics: MAE, RMSE, MAPE",
        "Slide 7": "Peer Review: 10-point checklist",
        "Slide 8": "Gantt Timeline: 10 task plan",
        "Slide 9": "Deployment: Flask + Docker",
        "Slide 10": "Next Steps: Real data, scaling to multi-store"
    }
    with open("outputs/slide_deck.md", "w", encoding="utf-8") as f:
        for k, v in slides.items():
            f.write(f"## {k}\n{v}\n\n")
