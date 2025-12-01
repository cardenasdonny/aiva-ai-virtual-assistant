from src.models.message import Message, Role, Conversation

def test_message_to_dict_roundtrip():
  msg = Message(role=Role.USER, content="Hello Aiva")

  data = msg.to_dict()
  assert data == {"role": "user", "content": "Hello Aiva"}

  #Rebuild from dict
  msg2 = Message.from_dict(data)
  assert msg2.role == Role.USER
  assert msg2.content == "Hello Aiva"

def test_conversation_add_and_last_user_message():
  conv = Conversation(mode="chat")

  conv.add_user_message("Hi")
  conv.add_aiva_message("Hello, how can I help?")

  assert len(conv.messages) == 2
  assert conv.last_user_message() == "Hi"

def test_conversation_to_dict_and_back():
  conv = Conversation(mode="chat")
  conv.add_user_message("First")
  conv.add_aiva_message("Reply")

  data = conv.to_dict()

  assert data["mode"] == "chat"
  assert len(data["messages"]) == 2

  restored = Conversation.from_dict(data)
  assert restored.mode == "chat"
  assert len(restored.messages) == 2
  assert restored.messages[0].content == "First"
  assert restored.messages[1].content == "Reply"