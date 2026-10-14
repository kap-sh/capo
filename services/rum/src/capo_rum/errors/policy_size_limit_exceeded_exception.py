"""Generated from Smithy shape ``com.amazonaws.rum#PolicySizeLimitExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_rum.errors import DeserializationError, ServiceError


class PolicySizeLimitExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: PolicySizeLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicySizeLimitExceededException_:
    out: PolicySizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PolicySizeLimitExceededException_.message required")
    return out


class PolicySizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#PolicySizeLimitExceededException``."""

    code: str | None = "PolicySizeLimitExceededException"

    def __init__(
        self,
        data: PolicySizeLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicySizeLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicySizeLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
