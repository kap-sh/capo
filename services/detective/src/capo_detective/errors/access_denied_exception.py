"""Generated from Smithy shape ``com.amazonaws.detective#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_detective.errors import ServiceError

if TYPE_CHECKING:
    import capo_detective.types.error_code
    import capo_detective.types.error_code_reason
    import capo_detective.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_detective.types.error_message.ErrorMessage"]
    error_code: NotRequired["capo_detective.types.error_code.ErrorCode"]
    """<p>The SDK default error code associated with the access denied exception.</p>"""
    error_code_reason: NotRequired[
        "capo_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p>The SDK default explanation of why access was denied.</p>"""
    sub_error_code: NotRequired["capo_detective.types.error_code.ErrorCode"]
    """<p>The error code associated with the access denied exception.</p>"""
    sub_error_code_reason: NotRequired[
        "capo_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p> An explanation of why access was denied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        import capo_detective.types.error_code

        out["ErrorCode"] = capo_detective.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_code_reason" in value:
        out["ErrorCodeReason"] = value["error_code_reason"]
    if "sub_error_code" in value:
        import capo_detective.types.error_code

        out["SubErrorCode"] = capo_detective.types.error_code.serialize_json(
            value["sub_error_code"]
        )
    if "sub_error_code_reason" in value:
        out["SubErrorCodeReason"] = value["sub_error_code_reason"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        import capo_detective.types.error_code

        out["error_code"] = capo_detective.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if data.get("ErrorCodeReason") is not None:
        out["error_code_reason"] = data["ErrorCodeReason"]
    if data.get("SubErrorCode") is not None:
        import capo_detective.types.error_code

        out["sub_error_code"] = capo_detective.types.error_code.deserialize_json(
            data["SubErrorCode"]
        )
    if data.get("SubErrorCodeReason") is not None:
        out["sub_error_code_reason"] = data["SubErrorCodeReason"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#AccessDeniedException``."""

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
