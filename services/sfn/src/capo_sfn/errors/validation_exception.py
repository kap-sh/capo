"""Generated from Smithy shape ``com.amazonaws.sfn#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message
    import capo_sfn.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "capo_sfn.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_sfn.types.validation_exception_reason

        out["reason"] = (
            capo_sfn.types.validation_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        import capo_sfn.types.validation_exception_reason

        out["reason"] = (
            capo_sfn.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ValidationException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
