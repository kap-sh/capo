"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelStreamError``."""

import json

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2._protocol.eventstream import HeaderValue, Message
from capo_sagemaker_runtime_http2.errors import ServiceError


class ModelStreamError_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelStreamError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ModelStreamError_:
    out: ModelStreamError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    return out


class ModelStreamError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelStreamError``."""

    code: str | None = "ModelStreamError"

    def __init__(
        self,
        data: ModelStreamError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelStreamError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ModelStreamError":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: ModelStreamError_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ModelStreamError",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ModelStreamError_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ModelStreamError_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
