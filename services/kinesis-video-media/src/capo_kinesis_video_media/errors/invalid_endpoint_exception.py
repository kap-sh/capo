"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#InvalidEndpointException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_media.types.error_message


class InvalidEndpointException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_video_media.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidEndpointException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidEndpointException_:
    out: InvalidEndpointException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidEndpointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideomedia#InvalidEndpointException``."""

    code: str | None = "InvalidEndpointException"

    def __init__(
        self,
        data: InvalidEndpointException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndpointException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidEndpointException":
        return cls(deserialize_json(data), message, response=response)
