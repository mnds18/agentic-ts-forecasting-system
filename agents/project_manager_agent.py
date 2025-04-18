"""
project_manager_agent.py
Project Manager Agent to build CSV plan and Gantt chart
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

def generate_plan_and_gantt():
    plan = pd.DataFrame([
        ("Requirement Gathering", "BA", 2, "2025-04-01", "2025-04-02", "Complete"),
        ("Data Generation", "DS", 1, "2025-04-03", "2025-04-03", "Complete"),
        ("Model Training", "DS", 2, "2025-04-04", "2025-04-05", "Complete"),
        ("Peer Review", "QA", 1, "2025-04-06", "2025-04-06", "Complete"),
        ("Documentation", "BA", 1, "2025-04-07", "2025-04-07", "Complete"),
        ("API Setup", "MLOps", 1, "2025-04-08", "2025-04-08", "Pending"),
        ("Gantt Chart", "PM", 1, "2025-04-09", "2025-04-09", "Pending"),
        ("Slides Prep", "BA", 1, "2025-04-10", "2025-04-10", "Pending"),
        ("Streamlit UI", "DS", 2, "2025-04-11", "2025-04-12", "Pending"),
        ("Dockerization", "MLOps", 2, "2025-04-13", "2025-04-14", "Pending")
    ], columns=["Task", "Owner", "Effort (hrs)", "Start", "Due", "Status"])

    os.makedirs("outputs", exist_ok=True)
    plan.to_csv("outputs/project_plan.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 4))
    for idx, row in plan.iterrows():
        ax.barh(row["Task"], pd.to_datetime(row["Due"]) - pd.to_datetime(row["Start"]), left=pd.to_datetime(row["Start"]))
    ax.set_title("📊 Gantt Chart: Project Timeline")
    ax.set_xlabel("Timeline")
    plt.tight_layout()
    plt.savefig("outputs/project_gantt.png")
    return plan


