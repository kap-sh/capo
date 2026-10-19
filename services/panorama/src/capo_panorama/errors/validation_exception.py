"""Generated from Smithy shape ``com.amazonaws.panorama#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import ServiceError

if TYPE_CHECKING:
    import capo_panorama.types.string
    import capo_panorama.types.validation_exception_error_argument_list
    import capo_panorama.types.validation_exception_field_list
    import capo_panorama.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_panorama.types.string.String"
    reason: NotRequired[
        "capo_panorama.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason that validation failed.</p>"""
    error_id: NotRequired["capo_panorama.types.string.String"]
    """<p>A unique ID for the error.</p>"""
    error_arguments: NotRequired[
        "capo_panorama.types.validation_exception_error_argument_list.ValidationExceptionErrorArgumentList"
    ]
    """<p>A list of attributes that led to the exception and their values.</p>"""
    fields: NotRequired[
        "capo_panorama.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of request parameters that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "error_id" in value:
        out["ErrorId"] = value["error_id"]
    if "error_arguments" in value:
        import capo_panorama.types.validation_exception_error_argument_list

        out["ErrorArguments"] = (
            capo_panorama.types.validation_exception_error_argument_list.serialize_json(
                value["error_arguments"]
            )
        )
    if "fields" in value:
        import capo_panorama.types.validation_exception_field_list

        out["Fields"] = (
            capo_panorama.types.validation_exception_field_list.serialize_json(
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
        out["reason"] = data["Reason"]
    if data.get("ErrorId") is not None:
        out["error_id"] = data["ErrorId"]
    if data.get("ErrorArguments") is not None:
        import capo_panorama.types.validation_exception_error_argument_list

        out["error_arguments"] = (
            capo_panorama.types.validation_exception_error_argument_list.deserialize_json(
                data["ErrorArguments"]
            )
        )
    if data.get("Fields") is not None:
        import capo_panorama.types.validation_exception_field_list

        out["fields"] = (
            capo_panorama.types.validation_exception_field_list.deserialize_json(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#ValidationException``."""

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
