"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListSyslogConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.list_syslog_configurations_max_results
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.vpc_endpoint_id


class ListSyslogConfigurationsRequest(TypedDict, closed=True):
    log_group_identifier: NotRequired[
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The name or ARN of the log group to filter syslog configurations for.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint to filter syslog configurations for.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. You received this token from a previous call.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.list_syslog_configurations_max_results.ListSyslogConfigurationsMaxResults"
    ]
    """<p>The maximum number of syslog configurations to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSyslogConfigurationsRequest) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSyslogConfigurationsRequest:
    out: ListSyslogConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
