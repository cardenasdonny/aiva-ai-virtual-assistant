from src.api.app import create_app


def test_chat_endpoint_returns_reply_and_conversation():
    app = create_app()
    client = app.test_client()

    payload = {"message": "Hello AIVA"}
    response = client.post("/api/chat", json=payload)

    assert response.status_code == 200
    data = response.get_json()

    # Basic shape
    assert "reply" in data
    assert "conversation" in data

    # Reply should reflect input and persona
    assert "Hello AIVA" in data["reply"]
    assert "AIVA" in data["reply"]

    # Conversation should contain both user and aiva messages
    conv = data["conversation"]
    assert conv["mode"] == "chat"
    assert len(conv["messages"]) == 2

    roles = [m["role"] for m in conv["messages"]]
    contents = [m["content"] for m in conv["messages"]]

    assert roles == ["user", "aiva"]
    assert contents[0] == "Hello AIVA"
    assert "Hello AIVA" in contents[1]