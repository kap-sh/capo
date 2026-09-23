"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentPayloadPart``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.attribution
    import capo_bedrock_agent_runtime.types.part_body


class InlineAgentPayloadPart(TypedDict, closed=True):
    bytes: NotRequired["capo_bedrock_agent_runtime.types.part_body.PartBody"]
    """<p>A part of the agent response in bytes.</p>"""
    attribution: NotRequired["capo_bedrock_agent_runtime.types.attribution.Attribution"]
    """<p>Contains citations for a part of an agent response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentPayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_bedrock_agent_runtime.types.part_body

        out["bytes"] = capo_bedrock_agent_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    if "attribution" in value:
        import capo_bedrock_agent_runtime.types.attribution

        out["attribution"] = (
            capo_bedrock_agent_runtime.types.attribution.serialize_json(
                value["attribution"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineAgentPayloadPart:
    out: InlineAgentPayloadPart = {}  # type: ignore[typeddict-item]
    if data.get("bytes") is not None:
        import capo_bedrock_agent_runtime.types.part_body

        out["bytes"] = capo_bedrock_agent_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    if data.get("attribution") is not None:
        import capo_bedrock_agent_runtime.types.attribution

        out["attribution"] = (
            capo_bedrock_agent_runtime.types.attribution.deserialize_json(
                data["attribution"]
            )
        )
    return out


def serialize_event_json(value: InlineAgentPayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "chunk",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InlineAgentPayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InlineAgentPayloadPart = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
