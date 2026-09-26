"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#TooManyRequestsException``."""

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import ServiceError


class TooManyRequestsException_(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The exception type.</p>"""
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambdamicrovms#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "TooManyRequestsException":
        return cls(deserialize_json(data), message)
