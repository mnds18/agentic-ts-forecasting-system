<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#F63366">
  <link rel="icon" href="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png">
  <title>Agentic TS Forecasting System</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen;
      line-height: 1.6;
      margin: 0;
      padding: 2rem;
      background-color: #f9f9fb;
      color: #1c1e21;
      transition: background-color 0.3s, color 0.3s;
    }
    header {
      background-color: #fff;
      padding: 1rem 2rem;
      border-bottom: 1px solid #eaeaea;
    }
    header img {
      height: 60px;
    }
    .badges img {
      margin-right: 0.5rem;
    }
    h1 {
      color: #F63366;
    }
    .theme-toggle {
      margin-top: 1rem;
    }
    .dark-theme {
      background-color: #121212;
      color: #f1f1f1;
    }
    .footer {
      margin-top: 3rem;
      font-size: 0.9rem;
      color: #777;
    }
    .contact {
      margin-top: 1rem;
    }
  </style>
</head>

<body>
  <header>
    <img src="https://github.com/mnds18/agentic-ts-forecasting-system/assets/your-image-id/banner.png" alt="Agentic AI Banner">
  </header>

  <main>
    <h1>Agentic Time Series Forecasting System</h1>

    <p>
      <strong>An enterprise-ready, multi-agent GenAI system for forecasting time series data.</strong>
      Built with LangChain-style architecture, Streamlit, Docker, Flask API, and Hugging Face Spaces.
    </p>

    <div class="badges">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
      <img src="https://github.com/mnds18/agentic-ts-forecasting-system/actions/workflows/python-app.yml/badge.svg" alt="CI Status">
      <img src="https://img.shields.io/badge/Streamlit-Dashboard-orange?logo=streamlit" alt="Streamlit">
      <img src="https://img.shields.io/badge/Spaces-HuggingFace-blue?logo=huggingface" alt="HF Spaces">
    </div>

    <div class="theme-toggle">
      <label>
        <input type="checkbox" id="themeToggle"> 🌗 Toggle Dark Mode
      </label>
    </div>

    <h2>Live Apps</h2>
    <ul>
      <li>📊 <a href="https://mnds18-agentic-ts-forecasting-system.streamlit.app">Streamlit Forecasting Dashboard</a></li>
      <li>🦙 <a href="https://huggingface.co/spaces/mnds18/agentic-ts-forecasting-system">Hugging Face Space</a></li>
    </ul>

    <h2>Quick Links</h2>
    <ul>
      <li><a href="../README.md">🔍 README Overview</a></li>
      <li><a href="../WIKI.md">📘 Architecture Wiki</a></li>
      <li><a href="../CONTRIBUTING.md">🤝 Contribution Guide</a></li>
    </ul>

    <h2>How to Use</h2>
    <p>
      Clone the repo, run the pipeline via <code>agentic_ts_forecasting_system.py</code>, and launch the dashboard with Streamlit.
    </p>

    <h2>About</h2>
    <p>
      Created by <strong>Mrig Debsarma</strong>, this system demonstrates how autonomous agents can manage business tasks like forecasting, documentation, peer review, and deployment — all orchestrated in Python.
    </p>

    <div class="contact">
      📫 Contact: <a href="mailto:mrig.debsarma@gmail.com">mrig.debsarma@gmail.com</a>
    </div>

    <div class="footer">
      &copy; 2025 Agentic AI Project — All rights reserved.
    </div>
  </main>

  <script>
    const toggle = document.getElementById('themeToggle');
    toggle.addEventListener('change', () => {
      document.body.classList.toggle('dark-theme');
    });
  </script>
</body>

</html>
