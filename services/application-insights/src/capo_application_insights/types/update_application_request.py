"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.attach_missing_permission
    import capo_application_insights.types.auto_config_enabled
    import capo_application_insights.types.cwe_monitor_enabled
    import capo_application_insights.types.ops_center_enabled
    import capo_application_insights.types.ops_item_sns_topic_arn
    import capo_application_insights.types.remove_sns_topic
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.sns_notification_arn


class UpdateApplicationRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    ops_center_enabled: NotRequired[
        "capo_application_insights.types.ops_center_enabled.OpsCenterEnabled"
    ]
    """<p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>"""
    cwe_monitor_enabled: NotRequired[
        "capo_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
    ]
    """<p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>"""
    ops_item_sns_topic_arn: NotRequired[
        "capo_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
    ]
    """<p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.</p>"""
    sns_notification_arn: NotRequired[
        "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS topic ARN. Allows you to receive SNS notifications for updates and issues with an application. </p>"""
    remove_sns_topic: NotRequired[
        "capo_application_insights.types.remove_sns_topic.RemoveSNSTopic"
    ]
    """<p> Disassociates the SNS topic from the opsItem created for detected problems.</p>"""
    auto_config_enabled: NotRequired[
        "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Turns auto-configuration on or off. </p>"""
    attach_missing_permission: NotRequired[
        "capo_application_insights.types.attach_missing_permission.AttachMissingPermission"
    ]
    """<p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "remove_sns_topic" in value:
        out["RemoveSNSTopic"] = value["remove_sns_topic"]
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("OpsCenterEnabled") is not None:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if data.get("CWEMonitorEnabled") is not None:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if data.get("OpsItemSNSTopicArn") is not None:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if data.get("RemoveSNSTopic") is not None:
        out["remove_sns_topic"] = data["RemoveSNSTopic"]
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if data.get("AttachMissingPermission") is not None:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out
