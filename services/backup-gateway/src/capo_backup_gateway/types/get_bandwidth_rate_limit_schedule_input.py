"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetBandwidthRateLimitScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn


class GetBandwidthRateLimitScheduleInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html"> <code>ListGateways</code> </a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBandwidthRateLimitScheduleInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBandwidthRateLimitScheduleInput:
    out: GetBandwidthRateLimitScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError(
            "GetBandwidthRateLimitScheduleInput.gateway_arn required"
        )
    return out
