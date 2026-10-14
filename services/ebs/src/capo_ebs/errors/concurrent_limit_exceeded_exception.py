"""Generated from Smithy shape ``com.amazonaws.ebs#ConcurrentLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ebs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ebs.types.error_message


class ConcurrentLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ebs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentLimitExceededException_:
    out: ConcurrentLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConcurrentLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#ConcurrentLimitExceededException``."""

    code: str | None = "ConcurrentLimitExceededException"

    def __init__(
        self,
        data: ConcurrentLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
