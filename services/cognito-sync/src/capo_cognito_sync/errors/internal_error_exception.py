"""Generated from Smithy shape ``com.amazonaws.cognitosync#InternalErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_cognito_sync.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class InternalErrorException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """Message returned by InternalErrorException."""


# --- restJson1 ser/de ---
def serialize_json(value: InternalErrorException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalErrorException_:
    out: InternalErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InternalErrorException``."""

    code: str | None = "InternalErrorException"

    def __init__(
        self,
        data: InternalErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalErrorException":
        return cls(deserialize_json(data), message, response=response)
