"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalStreamFailure``."""

import json

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2._protocol.eventstream import HeaderValue, Message
from capo_sagemaker_runtime_http2.errors import ServiceError


class InternalStreamFailure_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalStreamFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalStreamFailure_:
    out: InternalStreamFailure_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalStreamFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalStreamFailure``."""

    code: str | None = "InternalStreamFailure"

    def __init__(
        self,
        data: InternalStreamFailure_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalStreamFailure",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalStreamFailure":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: InternalStreamFailure_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "InternalStreamFailure",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InternalStreamFailure_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalStreamFailure_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
