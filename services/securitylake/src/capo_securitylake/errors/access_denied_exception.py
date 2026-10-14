"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessDeniedException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import ServiceError


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]
    error_code: NotRequired["str"]
    """<p>A coded string to provide more information about the access denied exception. You can use the error code to check the exception type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securitylake#AccessDeniedException``."""

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
