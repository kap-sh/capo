"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutBandwidthRateLimitScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn


class PutBandwidthRateLimitScheduleOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html"> <code>ListGateways</code> </a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutBandwidthRateLimitScheduleOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutBandwidthRateLimitScheduleOutput:
    out: PutBandwidthRateLimitScheduleOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    return out
