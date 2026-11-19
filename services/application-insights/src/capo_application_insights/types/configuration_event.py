"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.configuration_event_detail
    import capo_application_insights.types.configuration_event_monitored_resource_arn
    import capo_application_insights.types.configuration_event_resource_name
    import capo_application_insights.types.configuration_event_resource_type
    import capo_application_insights.types.configuration_event_status
    import capo_application_insights.types.configuration_event_time
    import capo_application_insights.types.resource_group_name


class ConfigurationEvent(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group of the application to which the configuration event belongs.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the application to which the configuration event belongs.</p>"""
    monitored_resource_arn: NotRequired[
        "capo_application_insights.types.configuration_event_monitored_resource_arn.ConfigurationEventMonitoredResourceARN"
    ]
    """<p> The resource monitored by Application Insights. </p>"""
    event_status: NotRequired[
        "capo_application_insights.types.configuration_event_status.ConfigurationEventStatus"
    ]
    """<p> The status of the configuration update event. Possible values include INFO, WARN, and ERROR. </p>"""
    event_resource_type: NotRequired[
        "capo_application_insights.types.configuration_event_resource_type.ConfigurationEventResourceType"
    ]
    """<p> The resource type that Application Insights attempted to configure, for example, CLOUDWATCH_ALARM. </p>"""
    event_time: NotRequired[
        "capo_application_insights.types.configuration_event_time.ConfigurationEventTime"
    ]
    """<p> The timestamp of the event. </p>"""
    event_detail: NotRequired[
        "capo_application_insights.types.configuration_event_detail.ConfigurationEventDetail"
    ]
    """<p> The details of the event in plain text. </p>"""
    event_resource_name: NotRequired[
        "capo_application_insights.types.configuration_event_resource_name.ConfigurationEventResourceName"
    ]
    """<p> The name of the resource Application Insights attempted to configure. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "monitored_resource_arn" in value:
        out["MonitoredResourceARN"] = value["monitored_resource_arn"]
    if "event_status" in value:
        import capo_application_insights.types.configuration_event_status

        out["EventStatus"] = (
            capo_application_insights.types.configuration_event_status.serialize_aws_json_1_1(
                value["event_status"]
            )
        )
    if "event_resource_type" in value:
        import capo_application_insights.types.configuration_event_resource_type

        out["EventResourceType"] = (
            capo_application_insights.types.configuration_event_resource_type.serialize_aws_json_1_1(
                value["event_resource_type"]
            )
        )
    if "event_time" in value:
        import capo_application_insights.types.configuration_event_time

        out["EventTime"] = (
            capo_application_insights.types.configuration_event_time.serialize_aws_json_1_1(
                value["event_time"]
            )
        )
    if "event_detail" in value:
        out["EventDetail"] = value["event_detail"]
    if "event_resource_name" in value:
        out["EventResourceName"] = value["event_resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("MonitoredResourceARN") is not None:
        out["monitored_resource_arn"] = data["MonitoredResourceARN"]
    if data.get("EventStatus") is not None:
        import capo_application_insights.types.configuration_event_status

        out["event_status"] = (
            capo_application_insights.types.configuration_event_status.deserialize_aws_json_1_1(
                data["EventStatus"]
            )
        )
    if data.get("EventResourceType") is not None:
        import capo_application_insights.types.configuration_event_resource_type

        out["event_resource_type"] = (
            capo_application_insights.types.configuration_event_resource_type.deserialize_aws_json_1_1(
                data["EventResourceType"]
            )
        )
    if data.get("EventTime") is not None:
        import capo_application_insights.types.configuration_event_time

        out["event_time"] = (
            capo_application_insights.types.configuration_event_time.deserialize_aws_json_1_1(
                data["EventTime"]
            )
        )
    if data.get("EventDetail") is not None:
        out["event_detail"] = data["EventDetail"]
    if data.get("EventResourceName") is not None:
        out["event_resource_name"] = data["EventResourceName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "monitored_resource_arn" in value:
        out["MonitoredResourceARN"] = value["monitored_resource_arn"]
    if "event_status" in value:
        import capo_application_insights.types.configuration_event_status

        out["EventStatus"] = (
            capo_application_insights.types.configuration_event_status.serialize_cbor(
                value["event_status"]
            )
        )
    if "event_resource_type" in value:
        import capo_application_insights.types.configuration_event_resource_type

        out["EventResourceType"] = (
            capo_application_insights.types.configuration_event_resource_type.serialize_cbor(
                value["event_resource_type"]
            )
        )
    if "event_time" in value:
        import capo_application_insights.types.configuration_event_time

        out["EventTime"] = (
            capo_application_insights.types.configuration_event_time.serialize_cbor(
                value["event_time"]
            )
        )
    if "event_detail" in value:
        out["EventDetail"] = value["event_detail"]
    if "event_resource_name" in value:
        out["EventResourceName"] = value["event_resource_name"]
    return out


def deserialize_cbor(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("MonitoredResourceARN") is not None:
        out["monitored_resource_arn"] = data["MonitoredResourceARN"]
    if data.get("EventStatus") is not None:
        import capo_application_insights.types.configuration_event_status

        out["event_status"] = (
            capo_application_insights.types.configuration_event_status.deserialize_cbor(
                data["EventStatus"]
            )
        )
    if data.get("EventResourceType") is not None:
        import capo_application_insights.types.configuration_event_resource_type

        out["event_resource_type"] = (
            capo_application_insights.types.configuration_event_resource_type.deserialize_cbor(
                data["EventResourceType"]
            )
        )
    if data.get("EventTime") is not None:
        import capo_application_insights.types.configuration_event_time

        out["event_time"] = (
            capo_application_insights.types.configuration_event_time.deserialize_cbor(
                data["EventTime"]
            )
        )
    if data.get("EventDetail") is not None:
        out["event_detail"] = data["EventDetail"]
    if data.get("EventResourceName") is not None:
        out["event_resource_name"] = data["EventResourceName"]
    return out
