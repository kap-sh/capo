"""Generated from Smithy shape ``com.amazonaws.kinesis#KMSAccessDeniedException``."""

import json
from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis._protocol.eventstream import HeaderValue, Message
from capo_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis.types.error_message


class KMSAccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSAccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSAccessDeniedException_:
    out: KMSAccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class KMSAccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#KMSAccessDeniedException``."""

    code: str | None = "KMSAccessDeniedException"

    def __init__(
        self,
        data: KMSAccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSAccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KMSAccessDeniedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)


def serialize_event_aws_json_1_1(value: KMSAccessDeniedException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "KMSAccessDeniedException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_1(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> KMSAccessDeniedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: KMSAccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_1(json.loads(payload))
    return out
