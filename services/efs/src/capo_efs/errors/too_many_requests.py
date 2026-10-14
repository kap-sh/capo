"""Generated from Smithy shape ``com.amazonaws.efs#TooManyRequests``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class TooManyRequests_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequests_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequests_:
    out: TooManyRequests_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("TooManyRequests_.error_code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TooManyRequests(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#TooManyRequests``."""

    code: str | None = "TooManyRequests"

    def __init__(
        self,
        data: TooManyRequests_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequests",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyRequests":
        return cls(deserialize_json(data), message, response=response)
