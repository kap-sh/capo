"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ValidationException``."""

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError, ServiceError


class ValidationException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The identifier of the resource that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pricingplanmanager#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ValidationException":
        return cls(deserialize_json(data), message)
