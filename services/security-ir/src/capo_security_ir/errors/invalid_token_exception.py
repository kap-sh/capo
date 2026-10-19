"""Generated from Smithy shape ``com.amazonaws.securityir#InvalidTokenException``."""

import zapros
from typing_extensions import TypedDict

from capo_security_ir.errors import ServiceError


class InvalidTokenException_(TypedDict, closed=True):
    message: "str"
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTokenException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidTokenException_:
    out: InvalidTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityir#InvalidTokenException``."""

    code: str | None = "InvalidTokenException"

    def __init__(
        self,
        data: InvalidTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="InvalidTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTokenException":
        return cls(deserialize_json(data), message, response=response)
