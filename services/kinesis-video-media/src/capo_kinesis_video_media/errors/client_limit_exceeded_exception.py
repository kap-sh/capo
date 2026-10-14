"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#ClientLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_media.types.error_message


class ClientLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_video_media.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ClientLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ClientLimitExceededException_:
    out: ClientLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ClientLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideomedia#ClientLimitExceededException``."""

    code: str | None = "ClientLimitExceededException"

    def __init__(
        self,
        data: ClientLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClientLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ClientLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
