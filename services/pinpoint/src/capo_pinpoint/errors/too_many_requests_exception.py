"""Generated from Smithy shape ``com.amazonaws.pinpoint#TooManyRequestsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_pinpoint.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API.</p>"""
    request_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request or response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestID") is not None:
        out["request_id"] = data["RequestID"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpoint#TooManyRequestsException``."""

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
