"""Generated from Smithy shape ``com.amazonaws.accountaccess#ValidationException``."""

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import ServiceError


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.accountaccess#ValidationException``."""

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
