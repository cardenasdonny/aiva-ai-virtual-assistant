import { useState } from "react";
import "./index.css";

const API_URL = "http://127.0.0.1:5000/api/chat"; // Flask backend

function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      from: "aiva",
      text: "Hi, I’m AIVA – your Python-focused AI Assistant. What would you like to explore today?",
    },
  ]);
  const [input, setInput] = useState("");
  const [isThinking, setIsThinking] = useState(false);

  async function handleSend(e) {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed || isThinking) return;

    const userMessage = {
      id: Date.now(),
      from: "user",
      text: trimmed,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsThinking(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: trimmed, mode: "chat" }),
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      const replyText = data.reply ?? "I’m not sure how to respond to that yet. 🙂";

      const aivaMessage = {
        id: Date.now() + 1,
        from: "aiva",
        text: replyText,
      };

      setMessages((prev) => [...prev, aivaMessage]);
    } catch (err) {
      const errorMessage = {
        id: Date.now() + 2,
        from: "aiva",
        text: "Something went wrong talking to the backend. Please check that the Flask server is running.",
      };
      setMessages((prev) => [...prev, errorMessage]);
      console.error(err);
    } finally {
      setIsThinking(false);
    }
  }

  return (
    <div className="app-root">
      <div className="app-shell">
        {/* LEFT: Chat */}
        <div className="chat-panel">
          <header className="chat-header">
            <div className="avatar-ring">
              <div className="avatar-face">
                <span className="avatar-eyes">• •</span>
                <span className="avatar-mouth">_</span>
              </div>
            </div>
            <div className="chat-title-block">
              <h1 className="chat-title">AIVA</h1>
              <p className="chat-subtitle">AI Virtual Assistant • Python & Dev Helper</p>
            </div>
          </header>

          <div className="chat-messages">
            {messages.map((msg) => (
              <div
                key={msg.id}
                className={
                  msg.from === "user" ? "bubble-row user-row" : "bubble-row aiva-row"
                }
              >
                {msg.from === "aiva" && (
                  <div className="mini-avatar" aria-hidden="true">
                    A
                  </div>
                )}
                <div
                  className={
                    msg.from === "user" ? "chat-bubble bubble-user" : "chat-bubble bubble-aiva"
                  }
                >
                  {msg.text}
                </div>
              </div>
            ))}

            {isThinking && (
              <div className="bubble-row aiva-row">
                <div className="mini-avatar" aria-hidden="true">
                  A
                </div>
                <div className="chat-bubble bubble-aiva thinking-bubble">
                  <span className="dot dot-1" />
                  <span className="dot dot-2" />
                  <span className="dot dot-3" />
                </div>
              </div>
            )}
          </div>

          <form className="chat-input-row" onSubmit={handleSend}>
            <input
              className="chat-input"
              placeholder="Ask AIVA about Python, clean code, architecture, testing…"
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
            <button className="send-button" type="submit" disabled={isThinking || !input.trim()}>
              {isThinking ? "Thinking…" : "Send"}
            </button>
          </form>

          <p className="hint-text">
            Tip: AIVA is currently using a fake AI engine – responses are generated locally. Backend
            can later be swapped to a real model.
          </p>
        </div>

        {/* RIGHT: Info / side panel */}
        <aside className="info-panel">
          <div className="info-card">
            <h2>About AIVA</h2>
            <p>
              AIVA is a learning project built with a clean architecture mindset: tested backend in
              Python + Flask and a modern React+Vite frontend.
            </p>
            <p>
              The assistant focuses on software topics: Python fundamentals, clean code practices,
              testing strategies, and project architecture.
            </p>
          </div>

          <div className="info-card">
            <h3>Tech stack</h3>
            <ul className="pill-list">
              <li>Python · Flask API</li>
              <li>React · Vite</li>
              <li>Clean Architecture</li>
              <li>TDD-backed backend</li>
            </ul>
          </div>

          <div className="info-card">
            <h3>Nice prompts to try</h3>
            <ul className="prompt-list">
              <li>“Help me refactor a messy Python function.”</li>
              <li>“Explain unit testing like I’m new to it.”</li>
              <li>“How would you structure a small CLI tool?”</li>
            </ul>
          </div>
        </aside>
      </div>
    </div>
  );
}

export default App;