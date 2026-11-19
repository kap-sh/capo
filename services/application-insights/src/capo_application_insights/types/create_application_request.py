"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.attach_missing_permission
    import capo_application_insights.types.auto_config_enabled
    import capo_application_insights.types.auto_create
    import capo_application_insights.types.cwe_monitor_enabled
    import capo_application_insights.types.grouping_type
    import capo_application_insights.types.ops_center_enabled
    import capo_application_insights.types.ops_item_sns_topic_arn
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.sns_notification_arn
    import capo_application_insights.types.tag_list


class CreateApplicationRequest(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
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
    """<p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem. </p>"""
    sns_notification_arn: NotRequired[
        "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS notification topic ARN. </p>"""
    tags: NotRequired["capo_application_insights.types.tag_list.TagList"]
    """<p>List of tags to add to the application. tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""
    auto_config_enabled: NotRequired[
        "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Indicates whether Application Insights automatically configures unmonitored resources in the resource group. </p>"""
    auto_create: NotRequired["capo_application_insights.types.auto_create.AutoCreate"]
    """<p> Configures all of the resources in the resource group by applying the recommended configurations. </p>"""
    grouping_type: NotRequired[
        "capo_application_insights.types.grouping_type.GroupingType"
    ]
    """<p>Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to <code>ACCOUNT_BASED</code>. </p>"""
    attach_missing_permission: NotRequired[
        "capo_application_insights.types.attach_missing_permission.AttachMissingPermission"
    ]
    """<p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "tags" in value:
        import capo_application_insights.types.tag_list

        out["Tags"] = capo_application_insights.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "auto_create" in value:
        out["AutoCreate"] = value["auto_create"]
    if "grouping_type" in value:
        import capo_application_insights.types.grouping_type

        out["GroupingType"] = (
            capo_application_insights.types.grouping_type.serialize_aws_json_1_1(
                value["grouping_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("OpsCenterEnabled") is not None:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if data.get("CWEMonitorEnabled") is not None:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if data.get("OpsItemSNSTopicArn") is not None:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if data.get("Tags") is not None:
        import capo_application_insights.types.tag_list

        out["tags"] = capo_application_insights.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if data.get("AutoCreate") is not None:
        out["auto_create"] = data["AutoCreate"]
    if data.get("GroupingType") is not None:
        import capo_application_insights.types.grouping_type

        out["grouping_type"] = (
            capo_application_insights.types.grouping_type.deserialize_aws_json_1_1(
                data["GroupingType"]
            )
        )
    if data.get("AttachMissingPermission") is not None:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "tags" in value:
        import capo_application_insights.types.tag_list

        out["Tags"] = capo_application_insights.types.tag_list.serialize_cbor(
            value["tags"]
        )
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "auto_create" in value:
        out["AutoCreate"] = value["auto_create"]
    if "grouping_type" in value:
        import capo_application_insights.types.grouping_type

        out["GroupingType"] = (
            capo_application_insights.types.grouping_type.serialize_cbor(
                value["grouping_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_cbor(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("OpsCenterEnabled") is not None:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if data.get("CWEMonitorEnabled") is not None:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if data.get("OpsItemSNSTopicArn") is not None:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if data.get("Tags") is not None:
        import capo_application_insights.types.tag_list

        out["tags"] = capo_application_insights.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if data.get("AutoCreate") is not None:
        out["auto_create"] = data["AutoCreate"]
    if data.get("GroupingType") is not None:
        import capo_application_insights.types.grouping_type

        out["grouping_type"] = (
            capo_application_insights.types.grouping_type.deserialize_cbor(
                data["GroupingType"]
            )
        )
    if data.get("AttachMissingPermission") is not None:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out
