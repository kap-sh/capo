"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteChimeWebhookConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn


class DeleteChimeWebhookConfigurationRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChimeWebhookConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteChimeWebhookConfigurationRequest:
    out: DeleteChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        out["chat_configuration_arn"] = ""
    return out
