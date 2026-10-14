"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#UnsupportedStreamMediaTypeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.error_message


class UnsupportedStreamMediaTypeException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedStreamMediaTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedStreamMediaTypeException_:
    out: UnsupportedStreamMediaTypeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnsupportedStreamMediaTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#UnsupportedStreamMediaTypeException``."""

    code: str | None = "UnsupportedStreamMediaTypeException"

    def __init__(
        self,
        data: UnsupportedStreamMediaTypeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedStreamMediaTypeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedStreamMediaTypeException":
        return cls(deserialize_json(data), message, response=response)
