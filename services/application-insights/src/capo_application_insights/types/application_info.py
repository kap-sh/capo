"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.attach_missing_permission
    import capo_application_insights.types.auto_config_enabled
    import capo_application_insights.types.cwe_monitor_enabled
    import capo_application_insights.types.discovery_type
    import capo_application_insights.types.life_cycle
    import capo_application_insights.types.ops_center_enabled
    import capo_application_insights.types.ops_item_sns_topic_arn
    import capo_application_insights.types.remarks
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.sns_notification_arn


class ApplicationInfo(TypedDict, closed=True):
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the application.</p>"""
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group used for the application.</p>"""
    life_cycle: NotRequired["capo_application_insights.types.life_cycle.LifeCycle"]
    """<p>The lifecycle of the application. </p>"""
    ops_item_sns_topic_arn: NotRequired[
        "capo_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
    ]
    """<p> The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates. </p>"""
    sns_notification_arn: NotRequired[
        "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS topic ARN that is associated with SNS notifications for updates or issues. </p>"""
    ops_center_enabled: NotRequired[
        "capo_application_insights.types.ops_center_enabled.OpsCenterEnabled"
    ]
    """<p> Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application. </p>"""
    cwe_monitor_enabled: NotRequired[
        "capo_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
    ]
    """<p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>"""
    remarks: NotRequired["capo_application_insights.types.remarks.Remarks"]
    """<p>The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:</p> <ul> <li> <p>“Configuring application, detected 1 Errors, 3 Warnings”</p> </li> <li> <p>“Configuring application, detected 1 Unconfigured Components”</p> </li> </ul>"""
    auto_config_enabled: NotRequired[
        "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
    ]
    """<p> Indicates whether auto-configuration is turned on for this application. </p>"""
    discovery_type: NotRequired[
        "capo_application_insights.types.discovery_type.DiscoveryType"
    ]
    """<p> The method used by Application Insights to onboard your resources. </p>"""
    attach_missing_permission: NotRequired[
        "capo_application_insights.types.attach_missing_permission.AttachMissingPermission"
    ]
    """<p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "life_cycle" in value:
        out["LifeCycle"] = value["life_cycle"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "remarks" in value:
        out["Remarks"] = value["remarks"]
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "discovery_type" in value:
        import capo_application_insights.types.discovery_type

        out["DiscoveryType"] = (
            capo_application_insights.types.discovery_type.serialize_aws_json_1_1(
                value["discovery_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("LifeCycle") is not None:
        out["life_cycle"] = data["LifeCycle"]
    if data.get("OpsItemSNSTopicArn") is not None:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if data.get("OpsCenterEnabled") is not None:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if data.get("CWEMonitorEnabled") is not None:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if data.get("Remarks") is not None:
        out["remarks"] = data["Remarks"]
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if data.get("DiscoveryType") is not None:
        import capo_application_insights.types.discovery_type

        out["discovery_type"] = (
            capo_application_insights.types.discovery_type.deserialize_aws_json_1_1(
                data["DiscoveryType"]
            )
        )
    if data.get("AttachMissingPermission") is not None:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "life_cycle" in value:
        out["LifeCycle"] = value["life_cycle"]
    if "ops_item_sns_topic_arn" in value:
        out["OpsItemSNSTopicArn"] = value["ops_item_sns_topic_arn"]
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    if "ops_center_enabled" in value:
        out["OpsCenterEnabled"] = value["ops_center_enabled"]
    if "cwe_monitor_enabled" in value:
        out["CWEMonitorEnabled"] = value["cwe_monitor_enabled"]
    if "remarks" in value:
        out["Remarks"] = value["remarks"]
    if "auto_config_enabled" in value:
        out["AutoConfigEnabled"] = value["auto_config_enabled"]
    if "discovery_type" in value:
        import capo_application_insights.types.discovery_type

        out["DiscoveryType"] = (
            capo_application_insights.types.discovery_type.serialize_cbor(
                value["discovery_type"]
            )
        )
    if "attach_missing_permission" in value:
        out["AttachMissingPermission"] = value["attach_missing_permission"]
    return out


def deserialize_cbor(data: dict) -> ApplicationInfo:
    out: ApplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("LifeCycle") is not None:
        out["life_cycle"] = data["LifeCycle"]
    if data.get("OpsItemSNSTopicArn") is not None:
        out["ops_item_sns_topic_arn"] = data["OpsItemSNSTopicArn"]
    if data.get("SNSNotificationArn") is not None:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    if data.get("OpsCenterEnabled") is not None:
        out["ops_center_enabled"] = data["OpsCenterEnabled"]
    if data.get("CWEMonitorEnabled") is not None:
        out["cwe_monitor_enabled"] = data["CWEMonitorEnabled"]
    if data.get("Remarks") is not None:
        out["remarks"] = data["Remarks"]
    if data.get("AutoConfigEnabled") is not None:
        out["auto_config_enabled"] = data["AutoConfigEnabled"]
    if data.get("DiscoveryType") is not None:
        import capo_application_insights.types.discovery_type

        out["discovery_type"] = (
            capo_application_insights.types.discovery_type.deserialize_cbor(
                data["DiscoveryType"]
            )
        )
    if data.get("AttachMissingPermission") is not None:
        out["attach_missing_permission"] = data["AttachMissingPermission"]
    return out
