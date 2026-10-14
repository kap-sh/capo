"""Generated from Smithy shape ``com.amazonaws.braket#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import ServiceError

if TYPE_CHECKING:
    import capo_braket.types.program_set_validation_failures_list
    import capo_braket.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "capo_braket.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for validation failure.</p>"""
    program_set_validation_failures: NotRequired[
        "capo_braket.types.program_set_validation_failures_list.ProgramSetValidationFailuresList"
    ]
    """<p>The validation failures in the program set submitted in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "program_set_validation_failures" in value:
        import capo_braket.types.program_set_validation_failures_list

        out["programSetValidationFailures"] = (
            capo_braket.types.program_set_validation_failures_list.serialize_json(
                value["program_set_validation_failures"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("programSetValidationFailures") is not None:
        import capo_braket.types.program_set_validation_failures_list

        out["program_set_validation_failures"] = (
            capo_braket.types.program_set_validation_failures_list.deserialize_json(
                data["programSetValidationFailures"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#ValidationException``."""

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
