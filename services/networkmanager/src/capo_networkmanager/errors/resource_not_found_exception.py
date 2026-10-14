"""Generated from Smithy shape ``com.amazonaws.networkmanager#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_networkmanager.types.exception_context_map
    import capo_networkmanager.types.server_side_string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    resource_id: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The ID of the resource.</p>"""
    resource_type: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The resource type.</p>"""
    context: NotRequired[
        "capo_networkmanager.types.exception_context_map.ExceptionContextMap"
    ]
    """<p>The specified resource could not be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "context" in value:
        import capo_networkmanager.types.exception_context_map

        out["Context"] = capo_networkmanager.types.exception_context_map.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    if data.get("Context") is not None:
        import capo_networkmanager.types.exception_context_map

        out["context"] = (
            capo_networkmanager.types.exception_context_map.deserialize_json(
                data["Context"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ResourceNotFoundException``."""

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
