"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteTeamsChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn


class DeleteTeamsChannelConfigurationRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTeamsChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteTeamsChannelConfigurationRequest:
    out: DeleteTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        out["chat_configuration_arn"] = ""
    return out
