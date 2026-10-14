"""Generated from Smithy shape ``com.amazonaws.polly#InvalidS3BucketException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message


class InvalidS3BucketException_(TypedDict, closed=True):
    message: NotRequired["capo_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidS3BucketException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidS3BucketException_:
    out: InvalidS3BucketException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidS3BucketException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#InvalidS3BucketException``."""

    code: str | None = "InvalidS3BucketException"

    def __init__(
        self,
        data: InvalidS3BucketException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3BucketException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidS3BucketException":
        return cls(deserialize_json(data), message, response=response)
