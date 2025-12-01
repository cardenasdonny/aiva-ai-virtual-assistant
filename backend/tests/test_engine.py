from src.core.engine import AivaEngine

def test_generate_reply_includes_user_message():
  engine = AivaEngine()

  reply = engine.generate_reply("Hello Aiva")

  assert "Hello Aiva" in reply
  assert "AIVA" in reply.upper()

def test_generate_reply_handles_empty_input():
  engine = AivaEngine()

  reply = engine.generate_reply(" ")

  #Should not crash, should give some friendly prompt
  assert "say something" in reply.lower() or "ask me" in reply.lower()