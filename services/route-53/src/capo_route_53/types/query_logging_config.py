"""Generated from Smithy shape ``com.amazonaws.route53#QueryLoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cloud_watch_logs_log_group_arn
    import capo_route_53.types.query_logging_config_id
    import capo_route_53.types.resource_id


class QueryLoggingConfig(TypedDict, closed=True):
    id: "capo_route_53.types.query_logging_config_id.QueryLoggingConfigId"
    """<p>The ID for a configuration for DNS query logging.</p>"""
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that CloudWatch Logs is logging queries for. </p>"""
    cloud_watch_logs_log_group_arn: (
        "capo_route_53.types.cloud_watch_logs_log_group_arn.CloudWatchLogsLogGroupArn"
    )
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryLoggingConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "CloudWatchLogsLogGroupArn").text = str(
        value["cloud_watch_logs_log_group_arn"]
    )


def deserialize_xml(el: Element) -> QueryLoggingConfig:
    out: QueryLoggingConfig = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        out["hosted_zone_id"] = ""
    child_cloud_watch_logs_log_group_arn = el.find("CloudWatchLogsLogGroupArn")
    if child_cloud_watch_logs_log_group_arn is not None:
        out["cloud_watch_logs_log_group_arn"] = str(
            child_cloud_watch_logs_log_group_arn.text or ""
        )
    else:
        out["cloud_watch_logs_log_group_arn"] = ""
    return out
