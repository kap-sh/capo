"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ConflictException``."""

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError


class ConflictException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The ID of the resource that is in conflict with the request.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource that is in conflict with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
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
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ConflictException":
        return cls(deserialize_json(data), message)
