"""Generated from Smithy shape ``com.amazonaws.sesv2#InvalidNextTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_sesv2.types.error_message


class InvalidNextTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_sesv2.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidNextTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sesv2#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(
        self,
        data: InvalidNextTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidNextTokenException":
        return cls(deserialize_json(data), message, response=response)
