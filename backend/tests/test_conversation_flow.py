"""
Tests the high-level assistant flow:
- user message goes into Conversation
- engine generates reply
- assistant reply is added to Conversation
"""

from src.core.engine import AivaEngine
from src.models.message import Conversation, Role


def test_conversation_flow_basic():
    conv = Conversation(mode="chat")
    engine = AivaEngine()

    # User sends a message
    user_msg = "Hello AIVA"
    conv.add_user_message(user_msg)

    # Engine generates reply (simulated)
    reply = engine.generate_reply(user_msg)

    # Add reply to conversation
    conv.add_aiva_message(reply)

    # Assertions
    assert conv.messages[0].role == Role.USER
    assert conv.messages[0].content == "Hello AIVA"

    assert conv.messages[1].role == Role.AIVA
    assert "Hello AIVA" in conv.messages[1].content # reply reflects input

    # Ensure last user message helper works
    assert conv.last_user_message() == "Hello AIVA"