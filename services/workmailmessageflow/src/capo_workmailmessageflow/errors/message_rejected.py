"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#MessageRejected``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workmailmessageflow.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.error_message


class MessageRejected_(TypedDict, closed=True):
    message: NotRequired["capo_workmailmessageflow.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageRejected_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MessageRejected_:
    out: MessageRejected_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MessageRejected(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmailmessageflow#MessageRejected``."""

    code: str | None = "MessageRejected"

    def __init__(
        self,
        data: MessageRejected_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MessageRejected",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MessageRejected":
        return cls(deserialize_json(data), message, response=response)
