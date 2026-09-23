"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeResponseStreamUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lambda.types.blob


class InvokeResponseStreamUpdate(TypedDict, closed=True):
    payload: NotRequired["capo_lambda.types.blob.Blob"]
    """<p>Data returned by your Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeResponseStreamUpdate) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InvokeResponseStreamUpdate:
    out: InvokeResponseStreamUpdate = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: InvokeResponseStreamUpdate) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "PayloadChunk",
        ":content-type": "application/octet-stream",
    }
    payload = b""
    payload = value["payload"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InvokeResponseStreamUpdate:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InvokeResponseStreamUpdate = {}  # type: ignore[typeddict-item]
    if payload:
        out["payload"] = payload
    return out
