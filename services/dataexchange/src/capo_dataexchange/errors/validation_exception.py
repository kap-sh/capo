"""Generated from Smithy shape ``com.amazonaws.dataexchange#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import ServiceError

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.exception_cause


class ValidationException_(TypedDict, closed=True):
    message: "capo_dataexchange.types.__string.__string"
    """<p>The message that informs you about what was invalid about the request.</p>"""
    exception_cause: NotRequired[
        "capo_dataexchange.types.exception_cause.ExceptionCause"
    ]
    """<p>The unique identifier for the resource that couldn't be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "exception_cause" in value:
        out["ExceptionCause"] = value["exception_cause"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ExceptionCause") is not None:
        out["exception_cause"] = data["ExceptionCause"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ValidationException``."""

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
