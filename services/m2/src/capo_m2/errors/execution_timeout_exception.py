"""Generated from Smithy shape ``com.amazonaws.m2#ExecutionTimeoutException``."""

import zapros
from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, ServiceError


class ExecutionTimeoutException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionTimeoutException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExecutionTimeoutException_:
    out: ExecutionTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ExecutionTimeoutException_.message required")
    return out


class ExecutionTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.m2#ExecutionTimeoutException``."""

    code: str | None = "ExecutionTimeoutException"

    def __init__(
        self,
        data: ExecutionTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="ExecutionTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExecutionTimeoutException":
        return cls(deserialize_json(data), message, response=response)
