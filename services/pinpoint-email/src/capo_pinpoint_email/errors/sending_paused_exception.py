"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendingPausedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.error_message


class SendingPausedException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint_email.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SendingPausedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SendingPausedException_:
    out: SendingPausedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SendingPausedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointemail#SendingPausedException``."""

    code: str | None = "SendingPausedException"

    def __init__(
        self,
        data: SendingPausedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SendingPausedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SendingPausedException":
        return cls(deserialize_json(data), message, response=response)
