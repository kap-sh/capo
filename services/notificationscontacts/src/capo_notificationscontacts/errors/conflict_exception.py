"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_notificationscontacts.errors import ServiceError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.error_message
    import capo_notificationscontacts.types.resource_id
    import capo_notificationscontacts.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: "capo_notificationscontacts.types.error_message.ErrorMessage"
    resource_id: "capo_notificationscontacts.types.resource_id.ResourceId"
    """<p>The resource ID that prompted the conflict error.</p>"""
    resource_type: "capo_notificationscontacts.types.resource_type.ResourceType"
    """<p>The resource type that prompted the conflict error.</p>"""


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
        out["message"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notificationscontacts#ConflictException``."""

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
