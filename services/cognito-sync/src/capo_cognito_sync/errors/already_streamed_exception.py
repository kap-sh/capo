"""Generated from Smithy shape ``com.amazonaws.cognitosync#AlreadyStreamedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_cognito_sync.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class AlreadyStreamedException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """The message associated with the AlreadyStreamedException exception."""


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyStreamedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyStreamedException_:
    out: AlreadyStreamedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class AlreadyStreamedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#AlreadyStreamedException``."""

    code: str | None = "AlreadyStreamedException"

    def __init__(
        self,
        data: AlreadyStreamedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyStreamedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AlreadyStreamedException":
        return cls(deserialize_json(data), message, response=response)
