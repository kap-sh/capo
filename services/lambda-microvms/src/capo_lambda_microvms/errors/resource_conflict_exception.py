"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ResourceConflictException``."""

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import ServiceError


class ResourceConflictException_(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The exception type.</p>"""
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConflictException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceConflictException_:
    out: ResourceConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdamicrovms#ResourceConflictException``."""

    code: str | None = "ResourceConflictException"

    def __init__(self, data: ResourceConflictException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceConflictException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ResourceConflictException":
        return cls(deserialize_json(data), message)
