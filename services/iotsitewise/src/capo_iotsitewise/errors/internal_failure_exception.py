"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InternalFailureException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message


class InternalFailureException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailureException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalFailureException_.message required")
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(self, data: InternalFailureException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InternalFailureException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: InternalFailureException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "internalFailureException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InternalFailureException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
