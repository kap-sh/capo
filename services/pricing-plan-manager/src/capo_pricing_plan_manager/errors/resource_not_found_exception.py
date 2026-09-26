"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ResourceNotFoundException``."""

from typing_extensions import TypedDict

from capo_pricing_plan_manager.errors import DeserializationError, ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The identifier of the resource that was not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
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
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pricingplanmanager#ResourceNotFoundException``."""

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
