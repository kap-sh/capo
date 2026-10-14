"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#InvalidResourceFormatException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video.types.error_message


class InvalidResourceFormatException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_video.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResourceFormatException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidResourceFormatException_:
    out: InvalidResourceFormatException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidResourceFormatException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideo#InvalidResourceFormatException``."""

    code: str | None = "InvalidResourceFormatException"

    def __init__(
        self,
        data: InvalidResourceFormatException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceFormatException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceFormatException":
        return cls(deserialize_json(data), message, response=response)
