"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#SessionExpiredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_signaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.error_message


class SessionExpiredException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_signaling.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SessionExpiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SessionExpiredException_:
    out: SessionExpiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SessionExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideosignaling#SessionExpiredException``."""

    code: str | None = "SessionExpiredException"

    def __init__(
        self,
        data: SessionExpiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionExpiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SessionExpiredException":
        return cls(deserialize_json(data), message, response=response)
