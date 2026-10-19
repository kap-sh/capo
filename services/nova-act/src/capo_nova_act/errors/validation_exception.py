"""Generated from Smithy shape ``com.amazonaws.novaact#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_nova_act.errors import ServiceError

if TYPE_CHECKING:
    import capo_nova_act.types.non_blank_string
    import capo_nova_act.types.validation_exception_field_list
    import capo_nova_act.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>The input fails to satisfy the constraints specified by the service.</p>"""
    reason: "capo_nova_act.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    field_list: NotRequired[
        "capo_nova_act.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of fields that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_nova_act.types.validation_exception_reason

    out["reason"] = capo_nova_act.types.validation_exception_reason.serialize_json(
        value["reason"]
    )
    if "field_list" in value:
        import capo_nova_act.types.validation_exception_field_list

        out["fieldList"] = (
            capo_nova_act.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_nova_act.types.validation_exception_reason

        out["reason"] = (
            capo_nova_act.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_nova_act.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    if data.get("fieldList") is not None:
        import capo_nova_act.types.validation_exception_field_list

        out["field_list"] = (
            capo_nova_act.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.novaact#ValidationException``."""

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
