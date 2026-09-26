"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AccessDeniedException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_iotsitewise.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: AccessDeniedException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "accessDeniedException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AccessDeniedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
