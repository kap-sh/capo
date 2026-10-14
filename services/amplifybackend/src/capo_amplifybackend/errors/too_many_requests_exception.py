"""Generated from Smithy shape ``com.amazonaws.amplifybackend#TooManyRequestsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_amplifybackend.errors import ServiceError

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class TooManyRequestsException_(TypedDict, closed=True):
    limit_type: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The type of limit that was exceeded.</p>"""
    message: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>An error message to inform that the request has failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "limit_type" in value:
        out["limitType"] = value["limit_type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("limitType") is not None:
        out["limit_type"] = data["limitType"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.amplifybackend#TooManyRequestsException``."""

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
            is_throttling_error=False,
            is_retryable=False,
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
