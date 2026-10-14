"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#MissingCodecPrivateDataException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.error_message


class MissingCodecPrivateDataException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MissingCodecPrivateDataException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MissingCodecPrivateDataException_:
    out: MissingCodecPrivateDataException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class MissingCodecPrivateDataException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#MissingCodecPrivateDataException``."""

    code: str | None = "MissingCodecPrivateDataException"

    def __init__(
        self,
        data: MissingCodecPrivateDataException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingCodecPrivateDataException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MissingCodecPrivateDataException":
        return cls(deserialize_json(data), message, response=response)
