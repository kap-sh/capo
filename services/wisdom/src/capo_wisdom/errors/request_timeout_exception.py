"""Generated from Smithy shape ``com.amazonaws.wisdom#RequestTimeoutException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import ServiceError


class RequestTimeoutException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestTimeoutException_:
    out: RequestTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RequestTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wisdom#RequestTimeoutException``."""

    code: str | None = "RequestTimeoutException"

    def __init__(
        self,
        data: RequestTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RequestTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestTimeoutException":
        return cls(deserialize_json(data), message, response=response)
