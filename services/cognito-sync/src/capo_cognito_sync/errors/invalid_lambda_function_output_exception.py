"""Generated from Smithy shape ``com.amazonaws.cognitosync#InvalidLambdaFunctionOutputException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_cognito_sync.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class InvalidLambdaFunctionOutputException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """<p>A message returned when an InvalidLambdaFunctionOutputException occurs</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidLambdaFunctionOutputException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidLambdaFunctionOutputException_:
    out: InvalidLambdaFunctionOutputException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidLambdaFunctionOutputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InvalidLambdaFunctionOutputException``."""

    code: str | None = "InvalidLambdaFunctionOutputException"

    def __init__(
        self,
        data: InvalidLambdaFunctionOutputException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLambdaFunctionOutputException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidLambdaFunctionOutputException":
        return cls(deserialize_json(data), message, response=response)
