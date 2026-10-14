"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsUserIdentitiesException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class ListMicrosoftTeamsUserIdentitiesException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsUserIdentitiesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsUserIdentitiesException_:
    out: ListMicrosoftTeamsUserIdentitiesException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ListMicrosoftTeamsUserIdentitiesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsUserIdentitiesException``."""

    code: str | None = "ListMicrosoftTeamsUserIdentitiesException"

    def __init__(
        self,
        data: ListMicrosoftTeamsUserIdentitiesException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ListMicrosoftTeamsUserIdentitiesException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ListMicrosoftTeamsUserIdentitiesException":
        return cls(deserialize_json(data), message, response=response)
