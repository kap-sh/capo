"""Generated from Smithy shape ``com.amazonaws.devopsguru#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_devops_guru.errors import ServiceError

if TYPE_CHECKING:
    import capo_devops_guru.types.error_message_string
    import capo_devops_guru.types.validation_exception_fields
    import capo_devops_guru.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_devops_guru.types.error_message_string.ErrorMessageString"
    """<p> A message that describes the validation exception. </p>"""
    reason: NotRequired[
        "capo_devops_guru.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p> The reason the validation exception was thrown. </p>"""
    fields: NotRequired[
        "capo_devops_guru.types.validation_exception_fields.ValidationExceptionFields"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_devops_guru.types.validation_exception_reason

        out["Reason"] = (
            capo_devops_guru.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_devops_guru.types.validation_exception_fields

        out["Fields"] = (
            capo_devops_guru.types.validation_exception_fields.serialize_json(
                value["fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_devops_guru.types.validation_exception_reason

        out["reason"] = (
            capo_devops_guru.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    if data.get("Fields") is not None:
        import capo_devops_guru.types.validation_exception_fields

        out["fields"] = (
            capo_devops_guru.types.validation_exception_fields.deserialize_json(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsguru#ValidationException``."""

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
