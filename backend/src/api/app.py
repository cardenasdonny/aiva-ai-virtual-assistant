"""
Flask API for AIVA Assistant.
"""

from flask import Flask, request, jsonify

from ..core.engine import AivaEngine
from ..models.message import Conversation


def create_app() -> Flask:
    """Factory that creates and configures the Flask app."""
    app = Flask(__name__)

    # AIVA engine
    engine = AivaEngine()

    # For now we use a conversation stored in memory
    conversation = Conversation(mode="chat")

    @app.post("/api/chat")
    def chat():
        data = request.get_json(force=True)
        user_msg = (data.get("message") or "").strip()

        # Update conversation
        conversation.add_user_message(user_msg)

        # Generate AI reply
        reply = engine.generate_reply(user_msg)
        conversation.add_aiva_message(reply)

        # Prepare response
        return jsonify({
            "reply": reply,
            "conversation": conversation.to_dict()
        })

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)