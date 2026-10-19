"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

import json
from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message
    import capo_iotsitewise.types.resource_arn
    import capo_iotsitewise.types.resource_id


class ConflictingOperationException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"
    resource_id: "capo_iotsitewise.types.resource_id.ResourceId"
    """<p>The ID of the resource that conflicts with this operation.</p>"""
    resource_arn: "capo_iotsitewise.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that conflicts with this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictingOperationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ConflictingOperationException_:
    out: ConflictingOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out


class ConflictingOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

    code: str | None = "ConflictingOperationException"

    def __init__(
        self,
        data: ConflictingOperationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictingOperationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictingOperationException":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: ConflictingOperationException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "conflictingOperationException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConflictingOperationException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConflictingOperationException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
