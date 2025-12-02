<h1 align="center">🚀 AIVA — AI Virtual Assistant (Python + Flask + React)</h1>

</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flask-API-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/React-Vite-61dafb?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Clean_Architecture-8a2be2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Testing-Pytest-brightgreen?style=for-the-badge" />
</p>

<hr />

<h2 align="center">✨ Overview</h2>

<p align="center">
AIVA (AI Virtual Assistant) is a full-stack project built with a clean, modular architecture using:
</p>

<div align="center">
<p>Python (Flask API)</p>
<p>React (Vite)</p>
<p>Test-Driven Development (Pytest)</p>
<p>Clean Architecture principles</p>
</div>

<p align="center">
AIVA runs fully locally — no external APIs are required.
The assistant’s responses are generated through an internal rule-based engine designed with TDD.
</p>

<p align="center">
The project includes a modern, futuristic UI consistent with previous projects such as:
</p>

<p align="center">
Smart Calculator
</p>

<p align="center">
Password Manager
</p>

<hr />

<h2 align="center">🎯 Key Features</h2>

<div align="center">

<strong>🔥 Local AI Engine</strong><br>
AIVA responds through a custom Python engine (AivaEngine), fully test-driven.

<br/>

<strong>⚡ Modern Full-Stack Setup</strong><br>
Separated Flask backend + React/Vite frontend.

<br/>

<strong>🧪 High Test Coverage</strong><br>
Unit tests cover:

Engine behavior

Message model

Conversation flow

API endpoints

<br/>

<strong>🎨 Premium UI Design</strong><br>
Dark futuristic interface with neon highlights.

<br/>

<strong>🔌 REST Chat API</strong><br>
Frontend communicates through /api/chat.

<br/>

<strong>🧼 Clean Architecture</strong><br>
Clearly separated layers ensure maintainability and scalability.

</div>

<hr />

<h2 align="center">🧠 Architecture</h2>

<pre align="center" style="text-align:left; display:inline-block; max-width:820px; padding:12px; background:#0b0b0b22; border-radius:8px;">
┌──────────────────────────┐
                         │ React UI │
                         │ (Vite + modern frontend) │
                         └───────────────┬──────────┘
                                         │
                                         ▼
                         ┌──────────────────────────┐
                         │ Flask API │
                         │ /api/chat endpoint │
                         └───────────────┬──────────┘
                                         │
                                         ▼
                         ┌──────────────────────────┐
                         │ AivaEngine.py │
                         │ Core logic + rule system │
                         └──────────────────────────┘
</pre>

<hr />

<h2 align="center">📁 Project Structure</h2>

<pre style="border-radius:8px; padding:14px; background:#0b0b0b08;">
aiva/
│
├── backend/
│ ├── src/
│ │ ├── api/
│ │ │ ├── app.py
│ │ │ └── __init__.py
│ │ ├── core/
│ │ │ ├── engine.py
│ │ ├── models/
│ │ │ ├── message.py
│ │ │ ├── conversation.py
│ │ └── __init__.py
│ │
│ ├── tests/
│ │ ├── test_api_chat.py
│ │ ├── test_conversation_flow.py
│ │ ├── test_engine.py
│ │ ├── test_message.py
│ │
│ └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── src/
    │ ├── App.jsx
    │ └── components/
    └── package.json
</pre>

<hr />

<h2 align="center">⚙️ Installation & Setup</h2>

<h3 align="center">1️⃣ Backend (Flask API)</h3>

<pre><code>cd backend
python3 -m venv venv
source venv/bin/activate # Linux/Mac
# OR venv\Scripts\activate # Windows

pip install -r requirements.txt
python3 -m src.api.app
</code></pre>

<hr />

<h3 align="center">2️⃣ Frontend (React + Vite)</h3>

<pre><code>cd frontend
npm install
npm run dev

Frontend default URL:

http://127.0.0.1:5173
</code></pre>

<hr />

<h2 align="center">🧪 Running Tests (TDD Workflow)</h2>

<pre><code>cd backend
pytest -q
</code></pre>

<p align="center">
Your test suite verifies:

Message object

Conversation tracking

Engine reply logic

API integration
</p>

<p align="center">
Everything was built using Test-Driven Development from day one.
</p>

<hr />

<h2 align="center">📡 API Reference</h2>

<p align="center"><strong>POST /api/chat</strong></p>

<pre><code>Request

{
  "message": "Hello AIVA"
}

Response

{
  "reply": "Hello! Great to hear from you 😊"
}
</code></pre>

<hr />

<h2 align="center">🖥️ Screenshots</h2>

<p align="center">
<img src="https://raw.githubusercontent.com/irmita-dev/aiva-ai-virtual-assistant/refs/heads/main/aiva_ai_virtual_assistant_demo_irmita_dev.png" width="65%" />
</p>

<hr />

<h2 align="center">🗺️ Roadmap</h2>

<p align="center">
✔️ Completed

Local rule-based AI engine

Flask API + React Vite frontend

TDD test suite

Clean architecture

Premium futuristic UI
</p>

<p align="center">
🚧 In Progress / Future Ideas

Replace engine with pluggable LLM

Persistent conversation memory

Voice mode (speech-to-text + TTS)

Docker support

Offline embedding-based reasoning
</p>

<hr />

<h2 align="center">👩‍💻 Author</h2>

<p align="center">
Irmita-dev<br>
Python developer focused on:
</p>

<p align="center">
- Clean Architecture
- TDD
- Full-Stack Engineering
- Modern UI/UX
</p>

<p align="center">
GitHub: https://github.com/irmita-dev
</p>

<hr />

<h2 align="center">📜 License</h2>

<p align="center">
MIT License
Feel free to use, modify, and build on this project.
</p>
