"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#InvalidArgumentException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_webrtc_storage.errors import ServiceError


class InvalidArgumentException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidArgumentException_:
    out: InvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#InvalidArgumentException``."""

    code: str | None = "InvalidArgumentException"

    def __init__(
        self,
        data: InvalidArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidArgumentException":
        return cls(deserialize_json(data), message, response=response)
