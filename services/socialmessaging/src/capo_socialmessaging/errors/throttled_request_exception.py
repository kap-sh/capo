"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ThrottledRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import ServiceError

if TYPE_CHECKING:
    import capo_socialmessaging.types.error_message


class ThrottledRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_socialmessaging.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledRequestException_:
    out: ThrottledRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ThrottledRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.socialmessaging#ThrottledRequestException``."""

    code: str | None = "ThrottledRequestException"

    def __init__(
        self,
        data: ThrottledRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottledRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottledRequestException":
        return cls(deserialize_json(data), message, response=response)
