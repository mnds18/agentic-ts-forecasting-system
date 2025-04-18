[![CI](https://github.com/mnds18/agentic-ts-forecasting-system/actions/workflows/python-app.yml/badge.svg)](https://github.com/mnds18/agentic-ts-forecasting-system/actions/workflows/python-app.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Dashboard-orange?logo=streamlit)](https://mnds18-agentic-ts-forecasting-system.streamlit.app)
[![Hugging Face](https://img.shields.io/badge/Spaces-HuggingFace-blue?logo=huggingface)](https://huggingface.co/spaces/mnds18/agentic-ts-forecasting-system)

# Agentic Time Series Forecasting System

This project showcases a modular, multi-agent GenAI system for time series forecasting using a retail sales use case. Designed for enterprise readiness and deployable on local machines, Docker, or cloud platforms.

---

## 🚀 Key Features
- **🧠 Agent-Oriented Architecture** — Each agent (BA, DS, Reviewer, MLOps, PM, Exec) mimics real roles
- **📈 Model Variety** — Prophet, ARIMA, and XGBoost (optional extensions)
- **🧪 Robust Testing** — Pytest-based unit tests with CI via GitHub Actions
- **📊 Live Dashboard** — Streamlit app with visual charts, error metrics, and execution logs
- **🔁 REST API** — Forecast serving via local Flask
- **📦 Docker Support** — Easily containerized for local/cloud deployment
- **📝 Markdown Reporting** — Agent-generated reports, plans, and presentations
- **🌐 GitHub Pages** — Public-facing docs, walkthroughs, and guides

---

## 💻 Quick Start

### 1. Clone and Set Up
```bash
git clone https://github.com/mnds18/agentic-ts-forecasting-system.git
cd agentic-ts-forecasting-system
pip install -r requirements.txt
```

### 2. Run Agentic Workflow
```bash
python agentic_ts_forecasting_system.py
```

### 3. View Streamlit Dashboard
```bash
streamlit run streamlit_app.py
```

### 4. Query Forecast via REST API
```bash
curl http://localhost:5001/forecast
```

---

## 🧪 Testing
Run all agent-level tests:
```bash
pytest -v test_agents.py
```

---

## 📦 Docker Deployment
```bash
docker build -t agentic-ts-app .
docker run -p 5001:5001 agentic-ts-app
```

---

## 🤗 Hugging Face Space
You can deploy this project to a Hugging Face Space:
- Create a new space under your account
- Set `sdk: streamlit`, point to `streamlit_app.py`
- Add required `requirements.txt` and optionally `Dockerfile`

👉 View: [https://huggingface.co/spaces/mnds18/agentic-ts-forecasting-system](https://huggingface.co/spaces/mnds18/agentic-ts-forecasting-system)

---

## 📘 Documentation
- [WIKI.md](WIKI.md) — System architecture, agent logic, flow diagrams
- [CONTRIBUTING.md](CONTRIBUTING.md) — Dev setup, issue flow, PR standards
- [LICENSE](LICENSE) — MIT License

---

## 🙌 Credits
Built with ❤️ by Mrig Debsarma and contributors.

> Inspired by enterprise-grade AI adoption in forecasting, orchestration, and intelligent automation.

---

## 📌 Welcome & Community

Hi there 👋 — and welcome to one of the most advanced open-source projects in **agentic AI and time series forecasting**!

This repo showcases an enterprise-ready, modular GenAI system using a multi-agent workflow, with live dashboards, documentation, Docker packaging, and Hugging Face deployment.

### 🔍 What You’ll Find Here
- **Streamlit Dashboard:**  📊 [Live Forecasting App](https://mnds18-agentic-ts-forecasting-system.streamlit.app)
- **Hugging Face Space:** 🤗 [Streamlit app](https://huggingface.co/spaces/mnds18/agentic-ts-forecasting-system)
- **Docs and Guides:** 📘 [WIKI.md](./WIKI.md), [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Agentic Workflow:** 🧠 [agentic_ts_forecasting_system.py](./agentic_ts_forecasting_system.py)
- **API Endpoint:** `GET /forecast` → [localhost:5001/forecast](http://localhost:5001/forecast)

### 🧪 How to Contribute
- Fork the repo
- Follow [CONTRIBUTING.md](./CONTRIBUTING.md)
- Run tests with `pytest`
- Open your first PR 🚀

### ⭐ Support This Project
- Star 🌟 the repo
- Share it with your network
- Submit issues for bugs, ideas, or improvements

Say hi below 👇 or request your first issue to be assigned.
Let’s build the future of autonomous AI workflows together!
