"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvocationOutput``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_iotsitewise.types.citations
    import capo_iotsitewise.types.string


class InvocationOutput(TypedDict, closed=True):
    message: NotRequired["capo_iotsitewise.types.string.String"]
    """<p>The text message of the SiteWise Assistant's response.</p>"""
    citations: NotRequired["capo_iotsitewise.types.citations.Citations"]
    """<p>A list of citations, and related information for the SiteWise Assistant's response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationOutput) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "citations" in value:
        import capo_iotsitewise.types.citations

        out["citations"] = capo_iotsitewise.types.citations.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> InvocationOutput:
    out: InvocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("citations") is not None:
        import capo_iotsitewise.types.citations

        out["citations"] = capo_iotsitewise.types.citations.deserialize_json(
            data["citations"]
        )
    return out


def serialize_event_json(value: InvocationOutput) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "output",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InvocationOutput:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InvocationOutput = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
