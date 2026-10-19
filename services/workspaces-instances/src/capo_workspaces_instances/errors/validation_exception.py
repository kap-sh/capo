"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces_instances.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_instances.types.validation_exception_field_list
    import capo_workspaces_instances.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    """<p>Overall description of validation failures.</p>"""
    reason: "capo_workspaces_instances.types.validation_exception_reason.ValidationExceptionReason"
    """<p>Specific reason for the validation failure.</p>"""
    field_list: NotRequired[
        "capo_workspaces_instances.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>List of fields that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_workspaces_instances.types.validation_exception_reason

    out["Reason"] = (
        capo_workspaces_instances.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_workspaces_instances.types.validation_exception_field_list

        out["FieldList"] = (
            capo_workspaces_instances.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_workspaces_instances.types.validation_exception_reason

        out["reason"] = (
            capo_workspaces_instances.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_workspaces_instances.types.validation_exception_reason.ValidationExceptionReason",
            "",
        )
    if data.get("FieldList") is not None:
        import capo_workspaces_instances.types.validation_exception_field_list

        out["field_list"] = (
            capo_workspaces_instances.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#ValidationException``."""

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
