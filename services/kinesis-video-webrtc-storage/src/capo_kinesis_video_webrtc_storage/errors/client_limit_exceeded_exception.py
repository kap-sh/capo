"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#ClientLimitExceededException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_webrtc_storage.errors import ServiceError


class ClientLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ClientLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ClientLimitExceededException_:
    out: ClientLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ClientLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#ClientLimitExceededException``."""

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
