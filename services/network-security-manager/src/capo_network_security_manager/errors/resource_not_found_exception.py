"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceNotFoundException``."""

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The ID of the resource that could not be found.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource that could not be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
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
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message)
