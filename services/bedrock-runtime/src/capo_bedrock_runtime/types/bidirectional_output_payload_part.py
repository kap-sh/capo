"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#BidirectionalOutputPayloadPart``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.part_body


class BidirectionalOutputPayloadPart(TypedDict, closed=True):
    bytes: NotRequired["capo_bedrock_runtime.types.part_body.PartBody"]
    """<p>The speech output of the bidirectional stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BidirectionalOutputPayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_bedrock_runtime.types.part_body

        out["bytes"] = capo_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> BidirectionalOutputPayloadPart:
    out: BidirectionalOutputPayloadPart = {}  # type: ignore[typeddict-item]
    if data.get("bytes") is not None:
        import capo_bedrock_runtime.types.part_body

        out["bytes"] = capo_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out


def serialize_event_json(value: BidirectionalOutputPayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "chunk",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BidirectionalOutputPayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BidirectionalOutputPayloadPart = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
