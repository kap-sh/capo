"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.arn
    import capo_chatbot.types.chime_webhook_description
    import capo_chatbot.types.chime_webhook_url
    import capo_chatbot.types.configuration_name
    import capo_chatbot.types.customer_cw_log_level
    import capo_chatbot.types.sns_topic_arn_list
    import capo_chatbot.types.tags


class CreateChimeWebhookConfigurationRequest(TypedDict, closed=True):
    webhook_description: (
        "capo_chatbot.types.chime_webhook_description.ChimeWebhookDescription"
    )
    """<p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    webhook_url: "capo_chatbot.types.chime_webhook_url.ChimeWebhookUrl"
    """<p>The URL for the Amazon Chime webhook.</p>"""
    sns_topic_arns: "capo_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    """<p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    iam_role_arn: "capo_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    configuration_name: "capo_chatbot.types.configuration_name.ConfigurationName"
    """<p>The name of the configuration.</p>"""
    logging_level: NotRequired[
        "capo_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
    ]
    """<p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>"""
    tags: NotRequired["capo_chatbot.types.tags.Tags"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChimeWebhookConfigurationRequest) -> dict:
    out: dict = {}
    out["WebhookDescription"] = value["webhook_description"]
    out["WebhookUrl"] = value["webhook_url"]
    import capo_chatbot.types.sns_topic_arn_list

    out["SnsTopicArns"] = capo_chatbot.types.sns_topic_arn_list.serialize_json(
        value["sns_topic_arns"]
    )
    out["IamRoleArn"] = value["iam_role_arn"]
    out["ConfigurationName"] = value["configuration_name"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "tags" in value:
        import capo_chatbot.types.tags

        out["Tags"] = capo_chatbot.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChimeWebhookConfigurationRequest:
    out: CreateChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebhookDescription") is not None:
        out["webhook_description"] = data["WebhookDescription"]
    else:
        raise DeserializationError(
            "CreateChimeWebhookConfigurationRequest.webhook_description required"
        )
    if data.get("WebhookUrl") is not None:
        out["webhook_url"] = data["WebhookUrl"]
    else:
        raise DeserializationError(
            "CreateChimeWebhookConfigurationRequest.webhook_url required"
        )
    if data.get("SnsTopicArns") is not None:
        import capo_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = capo_chatbot.types.sns_topic_arn_list.deserialize_json(
            data["SnsTopicArns"]
        )
    else:
        raise DeserializationError(
            "CreateChimeWebhookConfigurationRequest.sns_topic_arns required"
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "CreateChimeWebhookConfigurationRequest.iam_role_arn required"
        )
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
    else:
        raise DeserializationError(
            "CreateChimeWebhookConfigurationRequest.configuration_name required"
        )
    if data.get("LoggingLevel") is not None:
        out["logging_level"] = data["LoggingLevel"]
    if data.get("Tags") is not None:
        import capo_chatbot.types.tags

        out["tags"] = capo_chatbot.types.tags.deserialize_json(data["Tags"])
    return out
