"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.exception_message_content
    import capo_marketplace_catalog.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]
    validation_exception_field_list: NotRequired[
        "capo_marketplace_catalog.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of detailed entries describing the request fields that failed validation. Present when the failure can be attributed to one or more specific fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "validation_exception_field_list" in value:
        import capo_marketplace_catalog.types.validation_exception_field_list

        out["ValidationExceptionFieldList"] = (
            capo_marketplace_catalog.types.validation_exception_field_list.serialize_json(
                value["validation_exception_field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ValidationExceptionFieldList") is not None:
        import capo_marketplace_catalog.types.validation_exception_field_list

        out["validation_exception_field_list"] = (
            capo_marketplace_catalog.types.validation_exception_field_list.deserialize_json(
                data["ValidationExceptionFieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacecatalog#ValidationException``."""

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
