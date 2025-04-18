import os
import pytest
import pandas as pd
from agents import (
    requirements_agent,
    data_generation_agent,
    data_scientist_agent,
    peer_review_agent,
    documentation_agent,
    project_manager_agent,
    presentation_agent,
    orchestration_agent,
)

# ----------- Setup Fixtures ----------- #

@pytest.fixture(scope="module")
def dummy_sales_path():
    return "data/daily_sales.csv"

@pytest.fixture(scope="module")
def forecast_path():
    return "data/forecast.csv"

@pytest.fixture(scope="module")
def outputs_folder():
    return "outputs"

# ----------- Test Requirements Agent ----------- #

def test_requirements_output():
    result = requirements_agent.run_requirements_gathering()
    assert isinstance(result, dict)
    assert "granularity" in result  # Updated key
    assert os.path.exists("outputs/requirements_summary.json")

# ----------- Test Data Generation Agent ----------- #

def test_data_generation(dummy_sales_path):
    df = data_generation_agent.run_data_generation()
    assert isinstance(df, pd.DataFrame)
    assert os.path.exists(dummy_sales_path)
    assert len(df.columns) == 2 and "ds" in df.columns and "y" in df.columns
    assert df.shape[0] >= 1095  # Ensure 3 years of daily data

# ----------- Test Data Scientist Agent ----------- #

def test_forecast_training(forecast_path):
    forecast = data_scientist_agent.run_model_training()
    assert isinstance(forecast, pd.DataFrame)
    assert os.path.exists(forecast_path)
    assert "Model" in forecast.columns  # Updated expectation
    assert forecast.shape[0] >= 1

# ----------- Test Peer Review Agent ----------- #

def test_peer_review():
    df = peer_review_agent.run_peer_review()
    assert isinstance(df, pd.DataFrame)
    assert "Check" in df.columns
    assert "Status" in df.columns
    assert df.shape[0] >= 10
    assert df["Status"].isin(["Pass", "Fail"]).all()

# ----------- Test Documentation Agent ----------- #

def test_documentation_generated(outputs_folder):
    documentation_agent.generate_report()
    path = os.path.join(outputs_folder, "project_summary.md")
    assert os.path.exists(path)
    with open(path, encoding="utf-8") as f:
        content = f.read()
        assert "Executive Summary" in content

# ----------- Test Project Manager Agent ----------- #

def test_project_plan_created(outputs_folder):
    df = project_manager_agent.generate_plan_and_gantt()
    assert isinstance(df, pd.DataFrame)
    assert os.path.exists(os.path.join(outputs_folder, "project_plan.csv"))
    assert os.path.exists(os.path.join(outputs_folder, "project_gantt.png"))  # Corrected filename

# ----------- Test Presentation Agent ----------- #

def test_slides_created(outputs_folder):
    presentation_agent.generate_slide_deck()
    path = os.path.join(outputs_folder, "slide_deck.md")
    assert os.path.exists(path)
    with open(path, encoding="utf-8") as f:
        content = f.read()
        assert "Slide 1" in content

# ----------- Test Orchestration Logging ----------- #

def test_log_event():
    log_df = orchestration_agent.log_event(
        agent_name="Test Agent",
        step="mock_step",
        start_time=0,
        end_time=2,
        output_summary="Test summary"
    )
    assert isinstance(log_df, pd.DataFrame)
    assert os.path.exists("outputs/orchestration_log.csv")
    assert "Agent Name" in log_df.columns
    assert log_df.iloc[-1]["Agent Name"] == "Test Agent"
