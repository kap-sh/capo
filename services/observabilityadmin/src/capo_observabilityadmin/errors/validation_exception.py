"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import ServiceError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.validation_errors


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    errors: NotRequired[
        "capo_observabilityadmin.types.validation_errors.ValidationErrors"
    ]
    """<p> The errors in the input which caused the exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "errors" in value:
        import capo_observabilityadmin.types.validation_errors

        out["Errors"] = capo_observabilityadmin.types.validation_errors.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Errors") is not None:
        import capo_observabilityadmin.types.validation_errors

        out["errors"] = (
            capo_observabilityadmin.types.validation_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.observabilityadmin#ValidationException``."""

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
