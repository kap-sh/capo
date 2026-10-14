"""Generated from Smithy shape ``com.amazonaws.signin#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_signin.types.o_auth2_error_code


class AccessDeniedException_(TypedDict, closed=True):
    error: "capo_signin.types.o_auth2_error_code.OAuth2ErrorCode"
    """OAuth 2.0 error code indicating the specific type of access denial Can be TOKEN_EXPIRED, AUTHCODE_EXPIRED, USER_CREDENTIALS_CHANGED, or INSUFFICIENT_PERMISSIONS"""
    message: "str"
    """Detailed message explaining the access denial Provides specific information about why access was denied"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    import capo_signin.types.o_auth2_error_code

    out["error"] = capo_signin.types.o_auth2_error_code.serialize_json(value["error"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        import capo_signin.types.o_auth2_error_code

        out["error"] = capo_signin.types.o_auth2_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("AccessDeniedException_.error required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signin#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(
        self,
        data: AccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message, response=response)
