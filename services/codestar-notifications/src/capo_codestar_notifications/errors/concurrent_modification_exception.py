"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ConcurrentModificationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codestar_notifications.errors import ServiceError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.message


class ConcurrentModificationException_(TypedDict, closed=True):
    message: NotRequired["capo_codestar_notifications.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codestarnotifications#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(
        self,
        data: ConcurrentModificationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentModificationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentModificationException":
        return cls(deserialize_json(data), message, response=response)
