"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetBandwidthRateLimitScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.bandwidth_rate_limit_intervals
    import capo_backup_gateway.types.gateway_arn


class GetBandwidthRateLimitScheduleOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html"> <code>ListGateways</code> </a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    bandwidth_rate_limit_intervals: NotRequired[
        "capo_backup_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals"
    ]
    """<p>An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBandwidthRateLimitScheduleOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    if "bandwidth_rate_limit_intervals" in value:
        import capo_backup_gateway.types.bandwidth_rate_limit_intervals

        out["BandwidthRateLimitIntervals"] = (
            capo_backup_gateway.types.bandwidth_rate_limit_intervals.serialize_aws_json_1_0(
                value["bandwidth_rate_limit_intervals"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBandwidthRateLimitScheduleOutput:
    out: GetBandwidthRateLimitScheduleOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    if data.get("BandwidthRateLimitIntervals") is not None:
        import capo_backup_gateway.types.bandwidth_rate_limit_intervals

        out["bandwidth_rate_limit_intervals"] = (
            capo_backup_gateway.types.bandwidth_rate_limit_intervals.deserialize_aws_json_1_0(
                data["BandwidthRateLimitIntervals"]
            )
        )
    return out
