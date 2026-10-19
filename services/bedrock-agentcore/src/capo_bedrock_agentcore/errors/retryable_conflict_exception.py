"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RetryableConflictException``."""

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import ServiceError


class RetryableConflictException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RetryableConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RetryableConflictException_:
    out: RetryableConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class RetryableConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#RetryableConflictException``."""

    code: str | None = "RetryableConflictException"

    def __init__(
        self,
        data: RetryableConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RetryableConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RetryableConflictException":
        return cls(deserialize_json(data), message, response=response)
