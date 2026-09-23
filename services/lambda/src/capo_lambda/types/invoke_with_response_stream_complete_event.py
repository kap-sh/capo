"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamCompleteEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lambda.types.string


class InvokeWithResponseStreamCompleteEvent(TypedDict, closed=True):
    error_code: NotRequired["capo_lambda.types.string.String"]
    """<p>An error code.</p>"""
    error_details: NotRequired["capo_lambda.types.string.String"]
    """<p>The details of any returned error.</p>"""
    log_result: NotRequired["capo_lambda.types.string.String"]
    """<p>The last 4 KB of the execution log, which is base64-encoded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWithResponseStreamCompleteEvent) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_details" in value:
        out["ErrorDetails"] = value["error_details"]
    if "log_result" in value:
        out["LogResult"] = value["log_result"]
    return out


def deserialize_json(data: dict) -> InvokeWithResponseStreamCompleteEvent:
    out: InvokeWithResponseStreamCompleteEvent = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorDetails") is not None:
        out["error_details"] = data["ErrorDetails"]
    if data.get("LogResult") is not None:
        out["log_result"] = data["LogResult"]
    return out


def serialize_event_json(value: InvokeWithResponseStreamCompleteEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "InvokeComplete",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InvokeWithResponseStreamCompleteEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InvokeWithResponseStreamCompleteEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
