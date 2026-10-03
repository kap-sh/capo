"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackUserIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.arn
    import capo_chatbot.types.aws_user_identity
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.slack_team_id
    import capo_chatbot.types.slack_user_id


class SlackUserIdentity(TypedDict, closed=True):
    iam_role_arn: "capo_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration associated with the user identity to delete.</p>"""
    slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with AWS Chatbot.</p>"""
    slack_user_id: "capo_chatbot.types.slack_user_id.SlackUserId"
    """<p>The ID of the user in Slack</p>"""
    aws_user_identity: NotRequired[
        "capo_chatbot.types.aws_user_identity.AwsUserIdentity"
    ]
    """<p>The AWS user identity ARN used to associate a Slack user ID with an IAM Role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackUserIdentity) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["SlackTeamId"] = value["slack_team_id"]
    out["SlackUserId"] = value["slack_user_id"]
    if "aws_user_identity" in value:
        out["AwsUserIdentity"] = value["aws_user_identity"]
    return out


def deserialize_json(data: dict) -> SlackUserIdentity:
    out: SlackUserIdentity = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("SlackUserIdentity.iam_role_arn required")
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError("SlackUserIdentity.chat_configuration_arn required")
    if data.get("SlackTeamId") is not None:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        raise DeserializationError("SlackUserIdentity.slack_team_id required")
    if data.get("SlackUserId") is not None:
        out["slack_user_id"] = data["SlackUserId"]
    else:
        raise DeserializationError("SlackUserIdentity.slack_user_id required")
    if data.get("AwsUserIdentity") is not None:
        out["aws_user_identity"] = data["AwsUserIdentity"]
    return out
