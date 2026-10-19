"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteMicrosoftTeamsUserIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.uuid


class DeleteMicrosoftTeamsUserIdentityRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The ARN of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""
    user_id: "capo_chatbot.types.uuid.UUID"
    """<p>The Microsoft Teams user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrosoftTeamsUserIdentityRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> DeleteMicrosoftTeamsUserIdentityRequest:
    out: DeleteMicrosoftTeamsUserIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        out["chat_configuration_arn"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    return out
