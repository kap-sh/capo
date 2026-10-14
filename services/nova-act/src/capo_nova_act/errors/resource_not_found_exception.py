"""Generated from Smithy shape ``com.amazonaws.novaact#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_nova_act.types.non_blank_string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>The specified resource was not found.</p>"""
    resource_id: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>The identifier of the resource that wasn't found.</p>"""
    resource_type: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>The type of resource that wasn't found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.novaact#ResourceNotFoundException``."""

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
