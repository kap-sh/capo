"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#InvalidCodecPrivateDataException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.error_message


class InvalidCodecPrivateDataException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidCodecPrivateDataException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidCodecPrivateDataException_:
    out: InvalidCodecPrivateDataException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidCodecPrivateDataException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#InvalidCodecPrivateDataException``."""

    code: str | None = "InvalidCodecPrivateDataException"

    def __init__(
        self,
        data: InvalidCodecPrivateDataException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCodecPrivateDataException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCodecPrivateDataException":
        return cls(deserialize_json(data), message, response=response)
