"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces_thin_client.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.exception_message
    import capo_workspaces_thin_client.types.resource_id
    import capo_workspaces_thin_client.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_workspaces_thin_client.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired["capo_workspaces_thin_client.types.resource_id.ResourceId"]
    """<p>The ID of the resource associated with the request.</p>"""
    resource_type: NotRequired[
        "capo_workspaces_thin_client.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesthinclient#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message, response=response)
