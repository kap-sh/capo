"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn


class GetGatewayInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetGatewayInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetGatewayInput:
    out: GetGatewayInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        out["gateway_arn"] = ""
    return out
