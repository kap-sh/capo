"""Generated from Smithy shape ``com.amazonaws.inspectorscan#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_inspector_scan.errors import ServiceError

if TYPE_CHECKING:
    import capo_inspector_scan.types.validation_exception_fields
    import capo_inspector_scan.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_inspector_scan.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    fields: NotRequired[
        "capo_inspector_scan.types.validation_exception_fields.ValidationExceptionFields"
    ]
    """<p>The fields that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector_scan.types.validation_exception_reason

    out["reason"] = (
        capo_inspector_scan.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    if "fields" in value:
        import capo_inspector_scan.types.validation_exception_fields

        out["fields"] = (
            capo_inspector_scan.types.validation_exception_fields.serialize_json(
                value["fields"]
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
        import capo_inspector_scan.types.validation_exception_reason

        out["reason"] = (
            capo_inspector_scan.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_inspector_scan.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    if data.get("fields") is not None:
        import capo_inspector_scan.types.validation_exception_fields

        out["fields"] = (
            capo_inspector_scan.types.validation_exception_fields.deserialize_json(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspectorscan#ValidationException``."""

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
