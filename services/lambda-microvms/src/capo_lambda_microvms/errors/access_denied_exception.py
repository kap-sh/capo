"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#AccessDeniedException``."""

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdamicrovms#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message)
