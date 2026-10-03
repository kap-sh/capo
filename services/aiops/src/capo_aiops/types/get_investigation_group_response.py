"""Generated from Smithy shape ``com.amazonaws.aiops#GetInvestigationGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.chatbot_notification_channel
    import capo_aiops.types.cross_account_configurations
    import capo_aiops.types.encryption_configuration
    import capo_aiops.types.identifier_string_with_pattern_and_length_limits
    import capo_aiops.types.investigation_group_arn
    import capo_aiops.types.retention
    import capo_aiops.types.role_arn
    import capo_aiops.types.string_with_pattern_and_length_limits
    import capo_aiops.types.tag_key_boundaries


class GetInvestigationGroupResponse(TypedDict, closed=True):
    created_by: NotRequired[
        "capo_aiops.types.identifier_string_with_pattern_and_length_limits.IdentifierStringWithPatternAndLengthLimits"
    ]
    """<p>The name of the user who created the investigation group.</p>"""
    created_at: NotRequired["int"]
    """<p>The date and time that the investigation group was created.</p>"""
    last_modified_by: NotRequired[
        "capo_aiops.types.identifier_string_with_pattern_and_length_limits.IdentifierStringWithPatternAndLengthLimits"
    ]
    """<p>The name of the user who created the investigation group.</p>"""
    last_modified_at: NotRequired["int"]
    """<p>The date and time that the investigation group was most recently modified.</p>"""
    name: NotRequired[
        "capo_aiops.types.string_with_pattern_and_length_limits.StringWithPatternAndLengthLimits"
    ]
    """<p>The name of the investigation group.</p>"""
    arn: NotRequired["capo_aiops.types.investigation_group_arn.InvestigationGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the investigation group.</p>"""
    role_arn: NotRequired["capo_aiops.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that the investigation group uses for permissions to gather data.</p>"""
    encryption_configuration: NotRequired[
        "capo_aiops.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the customer managed KMS key that the investigation group uses to encrypt data, if there is one. If not, the investigation group uses an Amazon Web Services key to encrypt the data.</p>"""
    retention_in_days: NotRequired["capo_aiops.types.retention.Retention"]
    """<p>Specifies how long that investigation data is kept.</p>"""
    chatbot_notification_channel: NotRequired[
        "capo_aiops.types.chatbot_notification_channel.ChatbotNotificationChannel"
    ]
    """<p>This structure is a string array. The first string is the ARN of a Amazon SNS topic. The array of strings display the ARNs of chat applications configurations that are associated with that topic. For more information about these configuration ARNs, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html">Getting started with Amazon Q in chat applications</a> and <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies">Resource type defined by Amazon Web Services Chatbot</a>.</p>"""
    tag_key_boundaries: NotRequired[
        "capo_aiops.types.tag_key_boundaries.TagKeyBoundaries"
    ]
    """<p>Displays the custom tag keys for custom applications in your system that you have specified in the investigation group. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. </p>"""
    is_cloud_trail_event_history_enabled: NotRequired["bool"]
    """<p>Specifies whether CloudWatch investigationshas access to change events that are recorded by CloudTrail.</p>"""
    cross_account_configurations: NotRequired[
        "capo_aiops.types.cross_account_configurations.CrossAccountConfigurations"
    ]
    """<p>Lists the <code>AWSAccountId</code> of the accounts configured for cross-account access and the results of the last scan performed on each account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationGroupResponse) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        out["lastModifiedAt"] = value["last_modified_at"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "encryption_configuration" in value:
        import capo_aiops.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_aiops.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "retention_in_days" in value:
        out["retentionInDays"] = value["retention_in_days"]
    if "chatbot_notification_channel" in value:
        import capo_aiops.types.chatbot_notification_channel

        out["chatbotNotificationChannel"] = (
            capo_aiops.types.chatbot_notification_channel.serialize_json(
                value["chatbot_notification_channel"]
            )
        )
    if "tag_key_boundaries" in value:
        import capo_aiops.types.tag_key_boundaries

        out["tagKeyBoundaries"] = capo_aiops.types.tag_key_boundaries.serialize_json(
            value["tag_key_boundaries"]
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


def deserialize_json(data: dict) -> GetInvestigationGroupResponse:
    out: GetInvestigationGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        out["last_modified_at"] = data["lastModifiedAt"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("encryptionConfiguration") is not None:
        import capo_aiops.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_aiops.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    if data.get("chatbotNotificationChannel") is not None:
        import capo_aiops.types.chatbot_notification_channel

        out["chatbot_notification_channel"] = (
            capo_aiops.types.chatbot_notification_channel.deserialize_json(
                data["chatbotNotificationChannel"]
            )
        )
    if data.get("tagKeyBoundaries") is not None:
        import capo_aiops.types.tag_key_boundaries

        out["tag_key_boundaries"] = (
            capo_aiops.types.tag_key_boundaries.deserialize_json(
                data["tagKeyBoundaries"]
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
