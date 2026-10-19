"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteSlackUserIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.slack_team_id
    import capo_chatbot.types.slack_user_id


class DeleteSlackUserIdentityRequest(TypedDict, closed=True):
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The ARN of the SlackChannelConfiguration associated with the user identity to delete.</p>"""
    slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with AWS Chatbot.</p>"""
    slack_user_id: "capo_chatbot.types.slack_user_id.SlackUserId"
    """<p>The ID of the user in Slack</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackUserIdentityRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["SlackTeamId"] = value["slack_team_id"]
    out["SlackUserId"] = value["slack_user_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackUserIdentityRequest:
    out: DeleteSlackUserIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        out["chat_configuration_arn"] = ""
    if data.get("SlackTeamId") is not None:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        out["slack_team_id"] = ""
    if data.get("SlackUserId") is not None:
        out["slack_user_id"] = data["SlackUserId"]
    else:
        out["slack_user_id"] = ""
    return out
