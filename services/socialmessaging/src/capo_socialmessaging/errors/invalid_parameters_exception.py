"""Generated from Smithy shape ``com.amazonaws.socialmessaging#InvalidParametersException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import ServiceError

if TYPE_CHECKING:
    import capo_socialmessaging.types.error_message


class InvalidParametersException_(TypedDict, closed=True):
    message: NotRequired["capo_socialmessaging.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParametersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParametersException_:
    out: InvalidParametersException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidParametersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.socialmessaging#InvalidParametersException``."""

    code: str | None = "InvalidParametersException"

    def __init__(
        self,
        data: InvalidParametersException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParametersException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParametersException":
        return cls(deserialize_json(data), message, response=response)
