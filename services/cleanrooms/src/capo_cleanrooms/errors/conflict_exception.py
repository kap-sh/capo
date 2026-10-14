"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import ServiceError

if TYPE_CHECKING:
    import capo_cleanrooms.types.conflict_exception_reason
    import capo_cleanrooms.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_id: NotRequired["str"]
    """<p>The ID of the conflicting resource.</p>"""
    resource_type: NotRequired["capo_cleanrooms.types.resource_type.ResourceType"]
    """<p>The type of the conflicting resource.</p>"""
    reason: NotRequired[
        "capo_cleanrooms.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>A reason code for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanrooms#ConflictException``."""

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
