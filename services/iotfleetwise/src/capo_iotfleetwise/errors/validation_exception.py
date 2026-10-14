"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.string
    import capo_iotfleetwise.types.validation_exception_field_list
    import capo_iotfleetwise.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_iotfleetwise.types.string.string"
    reason: NotRequired[
        "capo_iotfleetwise.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason the input failed to satisfy the constraints specified by an Amazon Web Services service.</p>"""
    field_list: NotRequired[
        "capo_iotfleetwise.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of fields that fail to satisfy the constraints specified by an Amazon Web Services service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import capo_iotfleetwise.types.validation_exception_reason

        out["reason"] = (
            capo_iotfleetwise.types.validation_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_iotfleetwise.types.validation_exception_field_list

        out["fieldList"] = (
            capo_iotfleetwise.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("reason") is not None:
        import capo_iotfleetwise.types.validation_exception_reason

        out["reason"] = (
            capo_iotfleetwise.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    if data.get("fieldList") is not None:
        import capo_iotfleetwise.types.validation_exception_field_list

        out["field_list"] = (
            capo_iotfleetwise.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#ValidationException``."""

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
