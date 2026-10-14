"""Generated from Smithy shape ``com.amazonaws.synthetics#RequestEntityTooLargeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import ServiceError

if TYPE_CHECKING:
    import capo_synthetics.types.error_message


class RequestEntityTooLargeException_(TypedDict, closed=True):
    message: NotRequired["capo_synthetics.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestEntityTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestEntityTooLargeException_:
    out: RequestEntityTooLargeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class RequestEntityTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.synthetics#RequestEntityTooLargeException``."""

    code: str | None = "RequestEntityTooLargeException"

    def __init__(
        self,
        data: RequestEntityTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestEntityTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestEntityTooLargeException":
        return cls(deserialize_json(data), message, response=response)
