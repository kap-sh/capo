"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#PayloadPart``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.part_blob


class PayloadPart(TypedDict, closed=True):
    bytes: NotRequired["capo_sagemaker_runtime.types.part_blob.PartBlob"]
    """<p>A blob that contains part of the response for your streaming inference request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayloadPart) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PayloadPart:
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: PayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "PayloadPart",
        ":content-type": "application/octet-stream",
    }
    payload = b""
    payload = value["bytes"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    if payload:
        out["bytes"] = payload
    return out


def redact_sensitive(value: PayloadPart) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bytes" in value:
        out["bytes"] = "*** Sensitive Data Redacted ***"
    return out
