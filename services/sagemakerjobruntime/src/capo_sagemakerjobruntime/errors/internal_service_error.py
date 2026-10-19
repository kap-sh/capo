"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#InternalServiceError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_sagemakerjobruntime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.failure_reason


class InternalServiceError_(TypedDict, closed=True):
    message: "capo_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceError_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceError_:
    out: InternalServiceError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


class InternalServiceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#InternalServiceError``."""

    code: str | None = "InternalServiceError"

    def __init__(
        self,
        data: InternalServiceError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServiceError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServiceError":
        return cls(deserialize_json(data), message, response=response)
