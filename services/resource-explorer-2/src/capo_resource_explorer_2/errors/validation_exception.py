"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resource_explorer_2.errors import ServiceError

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: "str"
    field_list: NotRequired[
        "capo_resource_explorer_2.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>An array of the request fields that had validation errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "field_list" in value:
        import capo_resource_explorer_2.types.validation_exception_field_list

        out["FieldList"] = (
            capo_resource_explorer_2.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("FieldList") is not None:
        import capo_resource_explorer_2.types.validation_exception_field_list

        out["field_list"] = (
            capo_resource_explorer_2.types.validation_exception_field_list.deserialize_json(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourceexplorer2#ValidationException``."""

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
