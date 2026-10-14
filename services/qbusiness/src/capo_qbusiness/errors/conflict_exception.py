"""Generated from Smithy shape ``com.amazonaws.qbusiness#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_qbusiness.types.error_message
    import capo_qbusiness.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_qbusiness.types.error_message.ErrorMessage"
    """<p>The message describing a <code>ConflictException</code>.</p>"""
    resource_id: "capo_qbusiness.types.string.String"
    """<p>The identifier of the resource affected.</p>"""
    resource_type: "capo_qbusiness.types.string.String"
    """<p>The type of the resource affected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
