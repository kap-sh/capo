"""Generated from Smithy shape ``com.amazonaws.sso#InvalidRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sso.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso.types.error_description


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_sso.types.error_description.ErrorDescription"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sso#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(
        self,
        data: InvalidRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestException":
        return cls(deserialize_json(data), message, response=response)
