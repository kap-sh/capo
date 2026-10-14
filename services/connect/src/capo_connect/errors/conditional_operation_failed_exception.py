"""Generated from Smithy shape ``com.amazonaws.connect#ConditionalOperationFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class ConditionalOperationFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalOperationFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConditionalOperationFailedException_:
    out: ConditionalOperationFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConditionalOperationFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ConditionalOperationFailedException``."""

    code: str | None = "ConditionalOperationFailedException"

    def __init__(
        self,
        data: ConditionalOperationFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionalOperationFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConditionalOperationFailedException":
        return cls(deserialize_json(data), message, response=response)
