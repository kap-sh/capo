"""Generated from Smithy shape ``com.amazonaws.backupgateway#AssociateGatewayToServerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.server_arn


class AssociateGatewayToServerInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    server_arn: "capo_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateGatewayToServerInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    out["ServerArn"] = value["server_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateGatewayToServerInput:
    out: AssociateGatewayToServerInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        out["gateway_arn"] = ""
    if data.get("ServerArn") is not None:
        out["server_arn"] = data["ServerArn"]
    else:
        out["server_arn"] = ""
    return out
