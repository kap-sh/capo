"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamsChannelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.arn
    import capo_chatbot.types.boolean_account_preference
    import capo_chatbot.types.chat_configuration_arn
    import capo_chatbot.types.configuration_name
    import capo_chatbot.types.customer_cw_log_level
    import capo_chatbot.types.guardrail_policy_arn_list
    import capo_chatbot.types.resource_state
    import capo_chatbot.types.sns_topic_arn_list
    import capo_chatbot.types.string
    import capo_chatbot.types.tags
    import capo_chatbot.types.team_name
    import capo_chatbot.types.teams_channel_id
    import capo_chatbot.types.teams_channel_name
    import capo_chatbot.types.uuid


class TeamsChannelConfiguration(TypedDict, closed=True):
    channel_id: "capo_chatbot.types.teams_channel_id.TeamsChannelId"
    """<p>The ID of the Microsoft Teams channel.</p>"""
    channel_name: NotRequired["capo_chatbot.types.teams_channel_name.TeamsChannelName"]
    """<p>The name of the Microsoft Teams channel.</p>"""
    team_id: "capo_chatbot.types.uuid.UUID"
    """<p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    team_name: NotRequired["capo_chatbot.types.team_name.TeamName"]
    """<p>The name of the Microsoft Teams Team.</p>"""
    tenant_id: "capo_chatbot.types.uuid.UUID"
    """<p>The ID of the Microsoft Teams tenant.</p>"""
    chat_configuration_arn: (
        "capo_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""
    iam_role_arn: "capo_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    sns_topic_arns: "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    """<p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    configuration_name: NotRequired[
        "capo_chatbot.types.configuration_name.ConfigurationName"
    ]
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
    state: NotRequired["capo_chatbot.types.resource_state.ResourceState"]
    """<p>Either <code>ENABLED</code> or <code>DISABLED</code>. The resource returns <code>DISABLED</code> if the organization's AWS Chatbot policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.</p>"""
    state_reason: NotRequired["capo_chatbot.types.string.String"]
    """<p>Provided if State is <code>DISABLED</code>. Provides context as to why the resource is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TeamsChannelConfiguration) -> dict:
    out: dict = {}
    out["ChannelId"] = value["channel_id"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    out["TeamId"] = value["team_id"]
    if "team_name" in value:
        out["TeamName"] = value["team_name"]
    out["TenantId"] = value["tenant_id"]
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["IamRoleArn"] = value["iam_role_arn"]
    import capo_chatbot.types.sns_topic_arn_list

    out["SnsTopicArns"] = capo_chatbot.types.sns_topic_arn_list.serialize_json(
        value["sns_topic_arns"]
    )
    if "configuration_name" in value:
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
    if "state" in value:
        out["State"] = value["state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> TeamsChannelConfiguration:
    out: TeamsChannelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        raise DeserializationError("TeamsChannelConfiguration.channel_id required")
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    if data.get("TeamId") is not None:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError("TeamsChannelConfiguration.team_id required")
    if data.get("TeamName") is not None:
        out["team_name"] = data["TeamName"]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    else:
        raise DeserializationError("TeamsChannelConfiguration.tenant_id required")
    if data.get("ChatConfigurationArn") is not None:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "TeamsChannelConfiguration.chat_configuration_arn required"
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("TeamsChannelConfiguration.iam_role_arn required")
    if data.get("SnsTopicArns") is not None:
        import capo_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = capo_chatbot.types.sns_topic_arn_list.deserialize_json(
            data["SnsTopicArns"]
        )
    else:
        raise DeserializationError("TeamsChannelConfiguration.sns_topic_arns required")
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
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
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    return out
