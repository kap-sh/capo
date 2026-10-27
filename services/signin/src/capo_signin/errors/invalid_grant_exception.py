"""Generated from Smithy shape ``com.amazonaws.signin#InvalidGrantException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_signin.errors import ServiceError

if TYPE_CHECKING:
    import capo_signin.types.o_auth2_error_code


class InvalidGrantException_(TypedDict, closed=True):
    error: "capo_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """Will be invalid_grant."""
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidGrantException_) -> dict:
    out: dict = {}
    import capo_signin.types.o_auth2_error_code

    out["error"] = capo_signin.types.o_auth2_error_code.serialize_json(value["error"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidGrantException_:
    out: InvalidGrantException_ = {}  # type: ignore[typeddict-item]
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


class InvalidGrantException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#InvalidGrantException``."""

    code: str | None = "InvalidGrantException"

    def __init__(
        self,
        data: InvalidGrantException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidGrantException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidGrantException":
        return cls(deserialize_json(data), message, response=response)
