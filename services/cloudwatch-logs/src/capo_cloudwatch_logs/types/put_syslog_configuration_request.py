"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutSyslogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.vpc_endpoint_id


class PutSyslogConfigurationRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>The name or ARN of the log group to associate with the syslog configuration.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint to use for syslog ingestion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSyslogConfigurationRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSyslogConfigurationRequest:
    out: PutSyslogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    return out
