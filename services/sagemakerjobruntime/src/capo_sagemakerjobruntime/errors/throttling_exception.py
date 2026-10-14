"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_sagemakerjobruntime.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.failure_reason


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
