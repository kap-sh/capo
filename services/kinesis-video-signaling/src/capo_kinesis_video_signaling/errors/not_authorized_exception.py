"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#NotAuthorizedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_signaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.error_message


class NotAuthorizedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_signaling.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: NotAuthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotAuthorizedException_:
    out: NotAuthorizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NotAuthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideosignaling#NotAuthorizedException``."""

    code: str | None = "NotAuthorizedException"

    def __init__(
        self,
        data: NotAuthorizedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAuthorizedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotAuthorizedException":
        return cls(deserialize_json(data), message, response=response)
