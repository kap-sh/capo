"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.validation_exception_type


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    validation_exception_type: NotRequired[
        "capo_mediapackagev2.types.validation_exception_type.ValidationExceptionType"
    ]
    """<p>The type of ValidationException.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "validation_exception_type" in value:
        import capo_mediapackagev2.types.validation_exception_type

        out["ValidationExceptionType"] = (
            capo_mediapackagev2.types.validation_exception_type.serialize_json(
                value["validation_exception_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ValidationExceptionType") is not None:
        import capo_mediapackagev2.types.validation_exception_type

        out["validation_exception_type"] = (
            capo_mediapackagev2.types.validation_exception_type.deserialize_json(
                data["ValidationExceptionType"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediapackagev2#ValidationException``."""

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
