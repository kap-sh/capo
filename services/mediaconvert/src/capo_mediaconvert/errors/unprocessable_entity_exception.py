"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UnprocessableEntityException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediaconvert.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class UnprocessableEntityException_(TypedDict, closed=True):
    message: NotRequired["capo_mediaconvert.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessableEntityException_:
    out: UnprocessableEntityException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnprocessableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconvert#UnprocessableEntityException``."""

    code: str | None = "UnprocessableEntityException"

    def __init__(
        self,
        data: UnprocessableEntityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableEntityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnprocessableEntityException":
        return cls(deserialize_json(data), message, response=response)
