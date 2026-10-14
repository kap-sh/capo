"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ValidationError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.message


class ValidationError_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationError_:
    out: ValidationError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ValidationError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#ValidationError``."""

    code: str | None = "ValidationError"

    def __init__(
        self,
        data: ValidationError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationError":
        return cls(deserialize_json(data), message, response=response)
