"""Generated from Smithy shape ``com.amazonaws.iotsitewise#LimitExceededException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message


class LimitExceededException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LimitExceededException_.message required")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "LimitExceededException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: LimitExceededException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "limitExceededException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> LimitExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
