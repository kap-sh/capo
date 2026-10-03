"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateSlackChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.arn
    import capo_chatbot.types.boolean_account_preference
    import capo_chatbot.types.configuration_name
    import capo_chatbot.types.customer_cw_log_level
    import capo_chatbot.types.guardrail_policy_arn_list
    import capo_chatbot.types.slack_channel_display_name
    import capo_chatbot.types.slack_channel_id
    import capo_chatbot.types.slack_team_id
    import capo_chatbot.types.sns_topic_arn_list
    import capo_chatbot.types.tags


class CreateSlackChannelConfigurationRequest(TypedDict, closed=True):
    slack_team_id: "capo_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with AWS Chatbot.</p>"""
    slack_channel_id: "capo_chatbot.types.slack_channel_id.SlackChannelId"
    """<p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>"""
    slack_channel_name: NotRequired[
        "capo_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
    ]
    """<p>The name of the Slack channel.</p>"""
    sns_topic_arns: NotRequired["capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"]
    """<p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    iam_role_arn: "capo_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    configuration_name: "capo_chatbot.types.configuration_name.ConfigurationName"
    """<p>The name of the configuration.</p>"""
    logging_level: NotRequired[
        "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
    ]
    """<p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>"""
    guardrail_policy_arns: NotRequired[
        "capo_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
    ]
    """<p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>"""
    user_authorization_required: NotRequired[
        "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
    ]
    """<p>Enables use of a user role requirement in your chat configuration.</p>"""
    tags: NotRequired["capo_chatbot.types.tags.Tags"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlackChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["SlackTeamId"] = value["slack_team_id"]
    out["SlackChannelId"] = value["slack_channel_id"]
    if "slack_channel_name" in value:
        out["SlackChannelName"] = value["slack_channel_name"]
    if "sns_topic_arns" in value:
        import capo_chatbot.types.sns_topic_arn_list

        out["SnsTopicArns"] = capo_chatbot.types.sns_topic_arn_list.serialize_json(
            value["sns_topic_arns"]
        )
    out["IamRoleArn"] = value["iam_role_arn"]
    out["ConfigurationName"] = value["configuration_name"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "guardrail_policy_arns" in value:
        import capo_chatbot.types.guardrail_policy_arn_list

        out["GuardrailPolicyArns"] = (
            capo_chatbot.types.guardrail_policy_arn_list.serialize_json(
                value["guardrail_policy_arns"]
            )
        )
    if "user_authorization_required" in value:
        out["UserAuthorizationRequired"] = value["user_authorization_required"]
    if "tags" in value:
        import capo_chatbot.types.tags

        out["Tags"] = capo_chatbot.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSlackChannelConfigurationRequest:
    out: CreateSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SlackTeamId") is not None:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.slack_team_id required"
        )
    if data.get("SlackChannelId") is not None:
        out["slack_channel_id"] = data["SlackChannelId"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.slack_channel_id required"
        )
    if data.get("SlackChannelName") is not None:
        out["slack_channel_name"] = data["SlackChannelName"]
    if data.get("SnsTopicArns") is not None:
        import capo_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = capo_chatbot.types.sns_topic_arn_list.deserialize_json(
            data["SnsTopicArns"]
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.iam_role_arn required"
        )
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
    else:
        raise DeserializationError(
            "CreateSlackChannelConfigurationRequest.configuration_name required"
        )
    if data.get("LoggingLevel") is not None:
        out["logging_level"] = data["LoggingLevel"]
    if data.get("GuardrailPolicyArns") is not None:
        import capo_chatbot.types.guardrail_policy_arn_list

        out["guardrail_policy_arns"] = (
            capo_chatbot.types.guardrail_policy_arn_list.deserialize_json(
                data["GuardrailPolicyArns"]
            )
        )
    if data.get("UserAuthorizationRequired") is not None:
        out["user_authorization_required"] = data["UserAuthorizationRequired"]
    if data.get("Tags") is not None:
        import capo_chatbot.types.tags

        out["tags"] = capo_chatbot.types.tags.deserialize_json(data["Tags"])
    return out
