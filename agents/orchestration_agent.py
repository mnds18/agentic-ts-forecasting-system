"""
orchestration_agent.py
Tracks and logs execution time and outputs of each agent
"""

import csv
import os
import pandas as pd  # ✅ Required for DataFrame return
from datetime import datetime

LOG_PATH = "outputs/orchestration_log.csv"

def log_event(agent_name, step, start_time, end_time, output_summary):
    duration = round(end_time - start_time, 2)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(LOG_PATH)

    with open(LOG_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Timestamp", "Agent Name", "Step", "Start Time", "End Time", "Duration (s)", "Output Summary"])

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Timestamp": now,
            "Agent Name": agent_name,
            "Step": step,
            "Start Time": start_time,
            "End Time": end_time,
            "Duration (s)": duration,
            "Output Summary": output_summary
        })

    print(f"✅ {agent_name} completed in {duration}s | Output: {output_summary[:80]}...")
    return pd.read_csv(LOG_PATH)
