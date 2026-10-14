"""Generated from Smithy shape ``com.amazonaws.signin#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_signin.types.o_auth2_error_code


class InternalServerException_(TypedDict, closed=True):
    error: "capo_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating server error Will be SERVER_ERROR for internal server errors"""
    message: "str"
    """Detailed message explaining the server error May include error details for debugging purposes"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    import capo_signin.types.o_auth2_error_code

    out["error"] = capo_signin.types.o_auth2_error_code.serialize_json(value["error"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        import capo_signin.types.o_auth2_error_code

        out["error"] = capo_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("InternalServerException_.error required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message, response=response)
