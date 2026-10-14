"""Generated from Smithy shape ``com.amazonaws.qbusiness#MediaTooLargeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_qbusiness.types.error_message


class MediaTooLargeException_(TypedDict, closed=True):
    message: "capo_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: MediaTooLargeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MediaTooLargeException_:
    out: MediaTooLargeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("MediaTooLargeException_.message required")
    return out


class MediaTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#MediaTooLargeException``."""

    code: str | None = "MediaTooLargeException"

    def __init__(
        self,
        data: MediaTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MediaTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MediaTooLargeException":
        return cls(deserialize_json(data), message, response=response)
