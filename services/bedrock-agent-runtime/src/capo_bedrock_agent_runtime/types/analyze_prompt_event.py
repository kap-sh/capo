"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AnalyzePromptEvent``."""

import json

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message


class AnalyzePromptEvent(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>A message describing the analysis of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzePromptEvent) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AnalyzePromptEvent:
    out: AnalyzePromptEvent = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


def serialize_event_json(value: AnalyzePromptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "analyzePromptEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AnalyzePromptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AnalyzePromptEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
