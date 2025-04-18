# cli_runner.py
"""
Command-line interface to run any individual agent or full pipeline.
"""

import argparse
from agentic_ts_forecasting_system import run_pipeline
from agents import (
    requirements_agent,
    data_generation_agent,
    data_scientist_agent,
    peer_review_agent,
    documentation_agent,
    project_manager_agent,
    presentation_agent
)

def main():
    parser = argparse.ArgumentParser(description="Agentic AI CLI")
    parser.add_argument("--agent", type=str, help="Which agent to run individually")
    args = parser.parse_args()

    if not args.agent:
        run_pipeline()
        return

    agent_map = {
        "requirements": requirements_agent.run_requirements_gathering,
        "generation": data_generation_agent.run_data_generation,
        "training": data_scientist_agent.run_model_training,
        "review": peer_review_agent.run_peer_review,
        "report": documentation_agent.generate_report,
        "plan": project_manager_agent.generate_plan_and_gantt,
        "slides": presentation_agent.generate_slide_deck,
    }

    agent_fn = agent_map.get(args.agent.lower())
    if agent_fn:
        print(f"Running {args.agent} agent...")
        agent_fn()
    else:
        print("Invalid agent name. Available agents:", ", ".join(agent_map.keys()))

if __name__ == "__main__":
    main()
