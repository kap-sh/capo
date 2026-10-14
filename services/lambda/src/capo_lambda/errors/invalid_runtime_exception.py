"""Generated from Smithy shape ``com.amazonaws.lambda#InvalidRuntimeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class InvalidRuntimeException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRuntimeException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidRuntimeException_:
    out: InvalidRuntimeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidRuntimeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#InvalidRuntimeException``."""

    code: str | None = "InvalidRuntimeException"

    def __init__(
        self,
        data: InvalidRuntimeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRuntimeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRuntimeException":
        return cls(deserialize_json(data), message, response=response)
