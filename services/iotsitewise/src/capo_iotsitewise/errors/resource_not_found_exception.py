"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceNotFoundException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: ResourceNotFoundException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "resourceNotFoundException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ResourceNotFoundException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
