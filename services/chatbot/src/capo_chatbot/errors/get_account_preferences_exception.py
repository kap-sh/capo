"""Generated from Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class GetAccountPreferencesException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountPreferencesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetAccountPreferencesException_:
    out: GetAccountPreferencesException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class GetAccountPreferencesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesException``."""

    code: str | None = "GetAccountPreferencesException"

    def __init__(
        self,
        data: GetAccountPreferencesException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="GetAccountPreferencesException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GetAccountPreferencesException":
        return cls(deserialize_json(data), message, response=response)
