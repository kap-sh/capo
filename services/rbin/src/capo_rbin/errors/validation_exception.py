"""Generated from Smithy shape ``com.amazonaws.rbin#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rbin.errors import ServiceError

if TYPE_CHECKING:
    import capo_rbin.types.error_message
    import capo_rbin.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_rbin.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "capo_rbin.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_rbin.types.validation_exception_reason

        out["Reason"] = capo_rbin.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_rbin.types.validation_exception_reason

        out["reason"] = capo_rbin.types.validation_exception_reason.deserialize_json(
            data["Reason"]
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rbin#ValidationException``."""

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
