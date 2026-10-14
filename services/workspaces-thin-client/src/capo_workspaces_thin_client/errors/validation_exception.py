"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces_thin_client.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.exception_message
    import capo_workspaces_thin_client.types.validation_exception_field_list
    import capo_workspaces_thin_client.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_workspaces_thin_client.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "capo_workspaces_thin_client.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""
    field_list: NotRequired[
        "capo_workspaces_thin_client.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of fields that didn't validate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_workspaces_thin_client.types.validation_exception_reason

        out["reason"] = (
            capo_workspaces_thin_client.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_workspaces_thin_client.types.validation_exception_field_list

        out["fieldList"] = (
            capo_workspaces_thin_client.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        import capo_workspaces_thin_client.types.validation_exception_reason

        out["reason"] = (
            capo_workspaces_thin_client.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    if data.get("fieldList") is not None:
        import capo_workspaces_thin_client.types.validation_exception_field_list

        out["field_list"] = (
            capo_workspaces_thin_client.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesthinclient#ValidationException``."""

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
