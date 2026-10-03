"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestPayloadPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.types.sensitive_blob


class RequestPayloadPart(TypedDict, closed=True):
    bytes: NotRequired[
        "capo_sagemaker_runtime_http2.types.sensitive_blob.SensitiveBlob"
    ]
    """<p>The payload bytes.</p>"""
    data_type: NotRequired["str"]
    """<p>Data type header. Can be one of these possible values: "UTF8", "BINARY".</p>"""
    completion_state: NotRequired["str"]
    """<p>Completion state header. Can be one of these possible values: "PARTIAL", "COMPLETE".</p>"""
    p: NotRequired["str"]
    """<p>Padding string for alignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestPayloadPart) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RequestPayloadPart:
    out: RequestPayloadPart = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: RequestPayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "PayloadPart",
        ":content-type": "application/octet-stream",
    }
    payload = b""
    if "data_type" in value:
        headers["DataType"] = value["data_type"]
    if "completion_state" in value:
        headers["CompletionState"] = value["completion_state"]
    if "p" in value:
        headers["P"] = value["p"]
    payload = value["bytes"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> RequestPayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: RequestPayloadPart = {}  # type: ignore[typeddict-item]
    if "DataType" in headers:
        out["data_type"] = headers["DataType"]  # ty: ignore[invalid-assignment]
    if "CompletionState" in headers:
        out["completion_state"] = headers["CompletionState"]  # ty: ignore[invalid-assignment]
    if "P" in headers:
        out["p"] = headers["P"]  # ty: ignore[invalid-assignment]
    if payload:
        out["bytes"] = payload
    return out
