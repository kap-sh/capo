"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#MessageFrozen``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workmailmessageflow.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.error_message


class MessageFrozen_(TypedDict, closed=True):
    message: NotRequired["capo_workmailmessageflow.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageFrozen_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MessageFrozen_:
    out: MessageFrozen_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MessageFrozen(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmailmessageflow#MessageFrozen``."""

    code: str | None = "MessageFrozen"

    def __init__(
        self,
        data: MessageFrozen_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MessageFrozen",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MessageFrozen":
        return cls(deserialize_json(data), message, response=response)
