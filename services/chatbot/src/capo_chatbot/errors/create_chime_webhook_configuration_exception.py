"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class CreateChimeWebhookConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateChimeWebhookConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateChimeWebhookConfigurationException_:
    out: CreateChimeWebhookConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CreateChimeWebhookConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationException``."""

    code: str | None = "CreateChimeWebhookConfigurationException"

    def __init__(
        self,
        data: CreateChimeWebhookConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateChimeWebhookConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CreateChimeWebhookConfigurationException":
        return cls(deserialize_json(data), message, response=response)
