"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#NoDataRetentionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.error_message


class NoDataRetentionException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: NoDataRetentionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoDataRetentionException_:
    out: NoDataRetentionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NoDataRetentionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#NoDataRetentionException``."""

    code: str | None = "NoDataRetentionException"

    def __init__(
        self,
        data: NoDataRetentionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoDataRetentionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoDataRetentionException":
        return cls(deserialize_json(data), message, response=response)
