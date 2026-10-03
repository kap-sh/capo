"""Generated from Smithy shape ``com.amazonaws.aiops#UpdateInvestigationGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.chatbot_notification_channel
    import capo_aiops.types.cross_account_configurations
    import capo_aiops.types.encryption_configuration
    import capo_aiops.types.investigation_group_identifier
    import capo_aiops.types.role_arn
    import capo_aiops.types.tag_key_boundaries


class UpdateInvestigationGroupRequest(TypedDict, closed=True):
    identifier: (
        "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    )
    """<p>Specify either the name or the ARN of the investigation group that you want to modify.</p>"""
    role_arn: NotRequired["capo_aiops.types.role_arn.RoleArn"]
    """<p>Specify this field if you want to change the IAM role that CloudWatch investigations will use when it gathers investigation data. To do so, specify the ARN of the new role.</p> <p>The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data">How to control what data CloudWatch investigations has access to during investigations</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Use this structure if you want to use a customer managed KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an Amazon Web Services key to encrypt the data. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS">Encryption of investigation data</a>.</p>"""
    tag_key_boundaries: NotRequired[
        "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
    ]
    """<p>Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.</p> <p>You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.</p>"""
    chatbot_notification_channel: NotRequired[
        "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
    ]
    """<p>Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>"""
    is_cloud_trail_event_history_enabled: NotRequired["bool"]
    """<p>Specify <code>true</code> to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is <code>true</code>.</p>"""
    cross_account_configurations: NotRequired[
        "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
    ]
    """<p>Used to configure cross-account access for an investigation group. It allows the investigation group to access resources in other accounts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInvestigationGroupRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "encryption_configuration" in value:
        import capo_aiops.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_aiops.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tag_key_boundaries" in value:
        import capo_aiops.types.tag_key_boundaries

        out["tagKeyBoundaries"] = capo_aiops.types.tag_key_boundaries.serialize_json(
            value["tag_key_boundaries"]
        )
    if "chatbot_notification_channel" in value:
        import capo_aiops.types.chatbot_notification_channel

        out["chatbotNotificationChannel"] = (
            capo_aiops.types.chatbot_notification_channel.serialize_json(
                value["chatbot_notification_channel"]
            )
        )
    if "is_cloud_trail_event_history_enabled" in value:
        out["isCloudTrailEventHistoryEnabled"] = value[
            "is_cloud_trail_event_history_enabled"
        ]
    if "cross_account_configurations" in value:
        import capo_aiops.types.cross_account_configurations

        out["crossAccountConfigurations"] = (
            capo_aiops.types.cross_account_configurations.serialize_json(
                value["cross_account_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateInvestigationGroupRequest:
    out: UpdateInvestigationGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("encryptionConfiguration") is not None:
        import capo_aiops.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_aiops.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tagKeyBoundaries") is not None:
        import capo_aiops.types.tag_key_boundaries

        out["tag_key_boundaries"] = (
            capo_aiops.types.tag_key_boundaries.deserialize_json(
                data["tagKeyBoundaries"]
            )
        )
    if data.get("chatbotNotificationChannel") is not None:
        import capo_aiops.types.chatbot_notification_channel

        out["chatbot_notification_channel"] = (
            capo_aiops.types.chatbot_notification_channel.deserialize_json(
                data["chatbotNotificationChannel"]
            )
        )
    if data.get("isCloudTrailEventHistoryEnabled") is not None:
        out["is_cloud_trail_event_history_enabled"] = data[
            "isCloudTrailEventHistoryEnabled"
        ]
    if data.get("crossAccountConfigurations") is not None:
        import capo_aiops.types.cross_account_configurations

        out["cross_account_configurations"] = (
            capo_aiops.types.cross_account_configurations.deserialize_json(
                data["crossAccountConfigurations"]
            )
        )
    return out
