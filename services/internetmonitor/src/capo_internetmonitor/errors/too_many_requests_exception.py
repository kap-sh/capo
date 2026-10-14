"""Generated from Smithy shape ``com.amazonaws.internetmonitor#TooManyRequestsException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import ServiceError


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.internetmonitor#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(
        self,
        data: TooManyRequestsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="TooManyRequestsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyRequestsException":
        return cls(deserialize_json(data), message, response=response)
