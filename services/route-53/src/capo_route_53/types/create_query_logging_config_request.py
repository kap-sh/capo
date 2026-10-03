"""Generated from Smithy shape ``com.amazonaws.route53#CreateQueryLoggingConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.cloud_watch_logs_log_group_arn
    import capo_route_53.types.resource_id


class CreateQueryLoggingConfigRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.</p>"""
    cloud_watch_logs_log_group_arn: (
        "capo_route_53.types.cloud_watch_logs_log_group_arn.CloudWatchLogsLogGroupArn"
    )
    """<p>The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:</p> <p>arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> </p> <p>To get the ARN for a log group, you can use the CloudWatch console, the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html">DescribeLogGroups</a> API action, the <a href="https://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-groups.html">describe-log-groups</a> command, or the applicable command in one of the Amazon Web Services SDKs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateQueryLoggingConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "CloudWatchLogsLogGroupArn").text = str(
        value["cloud_watch_logs_log_group_arn"]
    )


def deserialize_xml(el: Element) -> CreateQueryLoggingConfigRequest:
    out: CreateQueryLoggingConfigRequest = {}  # type: ignore[typeddict-item]
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        raise DeserializationError(
            "CreateQueryLoggingConfigRequest.hosted_zone_id required"
        )
    child_cloud_watch_logs_log_group_arn = el.find("CloudWatchLogsLogGroupArn")
    if child_cloud_watch_logs_log_group_arn is not None:
        out["cloud_watch_logs_log_group_arn"] = str(
            child_cloud_watch_logs_log_group_arn.text or ""
        )
    else:
        raise DeserializationError(
            "CreateQueryLoggingConfigRequest.cloud_watch_logs_log_group_arn required"
        )
    return out
