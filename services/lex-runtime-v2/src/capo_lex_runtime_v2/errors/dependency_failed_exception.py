"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DependencyFailedException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.string


class DependencyFailedException_(TypedDict, closed=True):
    message: "capo_lex_runtime_v2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DependencyFailedException_.message required")
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimev2#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "DependencyFailedException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: DependencyFailedException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "DependencyFailedException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> DependencyFailedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
