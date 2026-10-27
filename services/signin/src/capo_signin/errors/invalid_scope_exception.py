"""Generated from Smithy shape ``com.amazonaws.signin#InvalidScopeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_signin.errors import ServiceError

if TYPE_CHECKING:
    import capo_signin.types.o_auth2_error_code


class InvalidScopeException_(TypedDict, closed=True):
    error: "capo_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """Will be invalid_scope."""
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidScopeException_) -> dict:
    out: dict = {}
    import capo_signin.types.o_auth2_error_code

    out["error"] = capo_signin.types.o_auth2_error_code.serialize_json(value["error"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidScopeException_:
    out: InvalidScopeException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        import capo_signin.types.o_auth2_error_code

        out["error"] = capo_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        import typing

        out["error"] = typing.cast(
            "capo_signin.types.o_auth2_error_code.OAuth2ErrorCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidScopeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#InvalidScopeException``."""

    code: str | None = "InvalidScopeException"

    def __init__(
        self,
        data: InvalidScopeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidScopeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidScopeException":
        return cls(deserialize_json(data), message, response=response)
