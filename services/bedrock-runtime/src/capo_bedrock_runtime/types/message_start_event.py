"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#MessageStartEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.conversation_role


class MessageStartEvent(TypedDict, closed=True):
    role: "capo_bedrock_runtime.types.conversation_role.ConversationRole"
    """<p>The role for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageStartEvent) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.conversation_role

    out["role"] = capo_bedrock_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    return out


def deserialize_json(data: dict) -> MessageStartEvent:
    out: MessageStartEvent = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_bedrock_runtime.types.conversation_role

        out["role"] = capo_bedrock_runtime.types.conversation_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("MessageStartEvent.role required")
    return out


def serialize_event_json(value: MessageStartEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "messageStart",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MessageStartEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MessageStartEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
