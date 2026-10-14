"""Generated from Smithy shape ``com.amazonaws.detective#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_detective.errors import ServiceError

if TYPE_CHECKING:
    import capo_detective.types.error_code
    import capo_detective.types.error_code_reason
    import capo_detective.types.error_message


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_detective.types.error_message.ErrorMessage"]
    error_code: NotRequired["capo_detective.types.error_code.ErrorCode"]
    """<p>The error code associated with the validation failure.</p>"""
    error_code_reason: NotRequired[
        "capo_detective.types.error_code_reason.ErrorCodeReason"
    ]
    """<p> An explanation of why validation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
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
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        import capo_detective.types.error_code

        out["error_code"] = capo_detective.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if data.get("ErrorCodeReason") is not None:
        out["error_code_reason"] = data["ErrorCodeReason"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_json(data), message, response=response)
