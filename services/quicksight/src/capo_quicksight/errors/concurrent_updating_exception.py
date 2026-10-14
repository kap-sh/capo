"""Generated from Smithy shape ``com.amazonaws.quicksight#ConcurrentUpdatingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class ConcurrentUpdatingException_(TypedDict, closed=True):
    message: NotRequired["capo_quicksight.types.string.String"]
    request_id: NotRequired["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentUpdatingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ConcurrentUpdatingException_:
    out: ConcurrentUpdatingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


class ConcurrentUpdatingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#ConcurrentUpdatingException``."""

    code: str | None = "ConcurrentUpdatingException"

    def __init__(
        self,
        data: ConcurrentUpdatingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentUpdatingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentUpdatingException":
        return cls(deserialize_json(data), message, response=response)
