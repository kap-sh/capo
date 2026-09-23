"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResponseChunk``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.content_delta_event
    import capo_bedrock_agentcore.types.content_start_event
    import capo_bedrock_agentcore.types.content_stop_event


class ResponseChunk(TypedDict, closed=True):
    content_start: NotRequired[
        "capo_bedrock_agentcore.types.content_start_event.ContentStartEvent"
    ]
    """<p>An event indicating the start of content streaming from the command execution. This is the first chunk received.</p>"""
    content_delta: NotRequired[
        "capo_bedrock_agentcore.types.content_delta_event.ContentDeltaEvent"
    ]
    """<p>An event containing incremental output (stdout or stderr) from the command execution. These are the middle chunks.</p>"""
    content_stop: NotRequired[
        "capo_bedrock_agentcore.types.content_stop_event.ContentStopEvent"
    ]
    """<p>An event indicating the completion of the command execution, including the exit code and final status. This is the last chunk received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseChunk) -> dict:
    out: dict = {}
    if "content_start" in value:
        import capo_bedrock_agentcore.types.content_start_event

        out["contentStart"] = (
            capo_bedrock_agentcore.types.content_start_event.serialize_json(
                value["content_start"]
            )
        )
    if "content_delta" in value:
        import capo_bedrock_agentcore.types.content_delta_event

        out["contentDelta"] = (
            capo_bedrock_agentcore.types.content_delta_event.serialize_json(
                value["content_delta"]
            )
        )
    if "content_stop" in value:
        import capo_bedrock_agentcore.types.content_stop_event

        out["contentStop"] = (
            capo_bedrock_agentcore.types.content_stop_event.serialize_json(
                value["content_stop"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseChunk:
    out: ResponseChunk = {}  # type: ignore[typeddict-item]
    if data.get("contentStart") is not None:
        import capo_bedrock_agentcore.types.content_start_event

        out["content_start"] = (
            capo_bedrock_agentcore.types.content_start_event.deserialize_json(
                data["contentStart"]
            )
        )
    if data.get("contentDelta") is not None:
        import capo_bedrock_agentcore.types.content_delta_event

        out["content_delta"] = (
            capo_bedrock_agentcore.types.content_delta_event.deserialize_json(
                data["contentDelta"]
            )
        )
    if data.get("contentStop") is not None:
        import capo_bedrock_agentcore.types.content_stop_event

        out["content_stop"] = (
            capo_bedrock_agentcore.types.content_stop_event.deserialize_json(
                data["contentStop"]
            )
        )
    return out


def serialize_event_json(value: ResponseChunk) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "chunk",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ResponseChunk:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ResponseChunk = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
