"""Generated from Smithy shape ``com.amazonaws.codeartifact#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codeartifact.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_codeartifact.types.string
    import capo_codeartifact.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_codeartifact.types.string.String"
    reason: NotRequired[
        "capo_codeartifact.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import capo_codeartifact.types.validation_exception_reason

        out["reason"] = (
            capo_codeartifact.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("reason") is not None:
        import capo_codeartifact.types.validation_exception_reason

        out["reason"] = (
            capo_codeartifact.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeartifact#ValidationException``."""

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
