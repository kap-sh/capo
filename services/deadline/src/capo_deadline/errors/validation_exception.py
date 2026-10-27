"""Generated from Smithy shape ``com.amazonaws.deadline#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import ServiceError

if TYPE_CHECKING:
    import capo_deadline.types.exception_context
    import capo_deadline.types.string
    import capo_deadline.types.validation_exception_field_list
    import capo_deadline.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_deadline.types.string.String"
    reason: "capo_deadline.types.validation_exception_reason.ValidationExceptionReason"
    """The reason that the request failed validation."""
    field_list: NotRequired[
        "capo_deadline.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """A list of fields that failed validation."""
    context: NotRequired["capo_deadline.types.exception_context.ExceptionContext"]
    """Information about the resources in use when the exception was thrown."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_deadline.types.validation_exception_reason

    out["reason"] = capo_deadline.types.validation_exception_reason.serialize_json(
        value["reason"]
    )
    if "field_list" in value:
        import capo_deadline.types.validation_exception_field_list

        out["fieldList"] = (
            capo_deadline.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    if "context" in value:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_deadline.types.validation_exception_reason

        out["reason"] = (
            capo_deadline.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_deadline.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    if data.get("fieldList") is not None:
        import capo_deadline.types.validation_exception_field_list

        out["field_list"] = (
            capo_deadline.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    if data.get("context") is not None:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ValidationException``."""

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
