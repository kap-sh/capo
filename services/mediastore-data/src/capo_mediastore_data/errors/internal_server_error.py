"""Generated from Smithy shape ``com.amazonaws.mediastoredata#InternalServerError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediastore_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore_data.types.error_message


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastoredata#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_json(data), message, response=response)
