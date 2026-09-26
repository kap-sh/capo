"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ConflictException``."""

from typing_extensions import TypedDict

from capo_pricing_plan_manager.errors import DeserializationError, ServiceError


class ConflictException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The identifier of the resource that has a conflicting state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pricingplanmanager#ConflictException``."""

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
