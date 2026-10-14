"""Generated from Smithy shape ``com.amazonaws.mediastoredata#RequestedRangeNotSatisfiableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediastore_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore_data.types.error_message


class RequestedRangeNotSatisfiableException_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestedRangeNotSatisfiableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestedRangeNotSatisfiableException_:
    out: RequestedRangeNotSatisfiableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class RequestedRangeNotSatisfiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastoredata#RequestedRangeNotSatisfiableException``."""

    code: str | None = "RequestedRangeNotSatisfiableException"

    def __init__(
        self,
        data: RequestedRangeNotSatisfiableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestedRangeNotSatisfiableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestedRangeNotSatisfiableException":
        return cls(deserialize_json(data), message, response=response)
