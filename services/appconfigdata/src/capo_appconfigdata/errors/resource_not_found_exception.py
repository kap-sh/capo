"""Generated from Smithy shape ``com.amazonaws.appconfigdata#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appconfigdata.errors import ServiceError

if TYPE_CHECKING:
    import capo_appconfigdata.types.resource_type
    import capo_appconfigdata.types.string
    import capo_appconfigdata.types.string_map


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_appconfigdata.types.string.String"]
    resource_type: NotRequired["capo_appconfigdata.types.resource_type.ResourceType"]
    """<p>The type of resource that was not found.</p>"""
    referenced_by: NotRequired["capo_appconfigdata.types.string_map.StringMap"]
    """<p>A map indicating which parameters in the request reference the resource that was not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "referenced_by" in value:
        import capo_appconfigdata.types.string_map

        out["ReferencedBy"] = capo_appconfigdata.types.string_map.serialize_json(
            value["referenced_by"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ReferencedBy") is not None:
        import capo_appconfigdata.types.string_map

        out["referenced_by"] = capo_appconfigdata.types.string_map.deserialize_json(
            data["ReferencedBy"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfigdata#ResourceNotFoundException``."""

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
