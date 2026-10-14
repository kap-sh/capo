"""Generated from Smithy shape ``com.amazonaws.codeartifact#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codeartifact.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_codeartifact.types.resource_type
    import capo_codeartifact.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_codeartifact.types.string.String"
    resource_id: NotRequired["capo_codeartifact.types.string.String"]
    """<p> The ID of the resource. </p>"""
    resource_type: NotRequired["capo_codeartifact.types.resource_type.ResourceType"]
    """<p> The type of Amazon Web Services resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_codeartifact.types.resource_type

        out["resourceType"] = capo_codeartifact.types.resource_type.serialize_json(
            value["resource_type"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        import capo_codeartifact.types.resource_type

        out["resource_type"] = capo_codeartifact.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeartifact#ResourceNotFoundException``."""

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
