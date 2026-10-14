"""Generated from Smithy shape ``com.amazonaws.s3tables#TooManyRequestsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3tables.types.error_message


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["capo_s3tables.types.error_message.ErrorMessage"]


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
    """Modeled error for Smithy shape ``com.amazonaws.s3tables#TooManyRequestsException``."""

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
