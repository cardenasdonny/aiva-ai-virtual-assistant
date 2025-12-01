"""
AIVA Engine - minimal fake AI logic for testing.
"""

class AivaEngine:
  """Minimal AI engine that returns simple persona-based replies."""

  def generate_reply(self, user_text: str) -> str:
    text = (user_text or "").strip()

    if not text:
      return "I'm AIVA ☺️ Please say something or ask me anything!"

    #Simple friendly echo logic
    return f"AIVA here ➡️ You said: '{text}'. How can I help next?"