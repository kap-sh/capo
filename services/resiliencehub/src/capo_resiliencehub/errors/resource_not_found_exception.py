"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import ServiceError

if TYPE_CHECKING:
    import capo_resiliencehub.types.resource_id
    import capo_resiliencehub.types.resource_type
    import capo_resiliencehub.types.string500


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    resource_id: NotRequired["capo_resiliencehub.types.resource_id.ResourceId"]
    """<p>The identifier of the resource that the exception applies to.</p>"""
    resource_type: NotRequired["capo_resiliencehub.types.resource_type.ResourceType"]
    """<p>The type of the resource that the exception applies to.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.resiliencehub#ResourceNotFoundException``."""

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
