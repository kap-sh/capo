"""Generated from Smithy shape ``com.amazonaws.polly#ThrottlingException``."""

import json
from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_polly._protocol.eventstream import HeaderValue, Message
from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.availability_error_message
    import capo_polly.types.throttling_reason_list


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_polly.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "capo_polly.types.throttling_reason_list.ThrottlingReasonList"
    ]
    """<p>A list of reasons explaining why the request was throttled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import capo_polly.types.throttling_reason_list

        out["throttlingReasons"] = (
            capo_polly.types.throttling_reason_list.serialize_json(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("throttlingReasons") is not None:
        import capo_polly.types.throttling_reason_list

        out["throttling_reasons"] = (
            capo_polly.types.throttling_reason_list.deserialize_json(
                data["throttlingReasons"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: ThrottlingException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ThrottlingException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ThrottlingException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
