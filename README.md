🚀 AIVA — AI Virtual Assistant (Python + Flask + React)

<p align="center">
  <img src="banner.png" width="100%" />
</p><br><p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flask-API-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/React-Vite-61dafb?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Clean_Architecture-8a2be2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Testing-Pytest-brightgreen?style=for-the-badge" />
</p>
---

✨ Overview

AIVA (AI Virtual Assistant) is a full-stack project built with a clean, modular architecture using:

Python (Flask API)

React (Vite)

Test-Driven Development (Pytest)

Clean Architecture principles


AIVA runs fully locally — no external APIs are required.
The assistant’s responses are generated through an internal rule-based engine designed with TDD.

The project includes a modern, futuristic UI consistent with previous projects such as:

Smart Calculator

Password Manager



---

🎯 Key Features

🔥 Local AI Engine
AIVA responds through a custom Python engine (AivaEngine), fully test-driven.

⚡ Modern Full-Stack Setup
Separated Flask backend + React/Vite frontend.

🧪 High Test Coverage
Unit tests cover:

Engine behavior

Message model

Conversation flow

API endpoints


🎨 Premium UI Design
Dark futuristic interface with neon highlights.

🔌 REST Chat API
Frontend communicates through /api/chat.

🧼 Clean Architecture
Clearly separated layers ensure maintainability and scalability.


---

🧠 Architecture

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


---

📁 Project Structure

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


---

⚙️ Installation & Setup

1️⃣ Backend (Flask API)

cd backend
python3 -m venv venv
source venv/bin/activate # Linux/Mac
# OR venv\Scripts\activate # Windows

pip install -r requirements.txt
python3 -m src.api.app

Backend default URL:

http://127.0.0.1:5001


---

2️⃣ Frontend (React + Vite)

cd frontend
npm install
npm run dev

Frontend default URL:

http://127.0.0.1:5173


---

🧪 Running Tests (TDD Workflow)

cd backend
pytest -q

Your test suite verifies:

Message object

Conversation tracking

Engine reply logic

API integration


Everything was built using Test-Driven Development from day one.


---

📡 API Reference

POST /api/chat

Request

{
  "message": "Hello AIVA"
}

Response

{
  "reply": "Hello! Great to hear from you 😊"
}


---

🖥️ Screenshots

> Add images here (UI preview, conversation demo, etc.)




---

🗺️ Roadmap

✔️ Completed

Local rule-based AI engine

Flask API + React Vite frontend

TDD test suite

Clean architecture

Premium futuristic UI


🚧 In Progress / Future Ideas

Replace engine with pluggable LLM

Persistent conversation memory

Voice mode (speech-to-text + TTS)

Docker support

Offline embedding-based reasoning



---

👩‍💻 Author

Irmina — irmita-dev
Self-taught Python developer focused on:

Clean Architecture

TDD

Full-Stack Engineering

Modern UI/UX


GitHub: https://github.com/irmita-dev


---

📜 License

MIT License
Feel free to use, modify, and build on this project.