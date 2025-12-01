"""
Core conversation models for AIVA.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any


class Role(str, Enum):
    """Role of a message in the conversation."""
    USER = "user"
    AIVA = "aiva"
    SYSTEM = "system"


@dataclass
class Message:
    """Single message in the conversation."""
    role: Role
    content: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "role": self.role.value,
            "content": self.content,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Message":
        return cls(
            role=Role(data["role"]),
            content=data["content"],
        )


@dataclass
class Conversation:
    """Conversation with AIVA in a given mode (e.g. 'chat', 'coder')."""
    mode: str
    messages: List[Message] = field(default_factory=list)

    def add_user_message(self, content: str) -> None:
        self.messages.append(Message(role=Role.USER, content=content))

    def add_aiva_message(self, content: str) -> None:
        self.messages.append(Message(role=Role.AIVA, content=content))

    def last_user_message(self) -> str:
        """Return the last user message content or empty string."""
        for msg in reversed(self.messages):
            if msg.role is Role.USER:
                return msg.content
        return ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mode": self.mode,
            "messages": [m.to_dict() for m in self.messages],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Conversation":
        conv = cls(mode=data.get("mode", ""))
        for m in data.get("messages", []):
            conv.messages.append(Message.from_dict(m))
        return conv