"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutMaintenanceStartTimeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn


class PutMaintenanceStartTimeOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of a gateway for which you set the maintenance start time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMaintenanceStartTimeOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMaintenanceStartTimeOutput:
    out: PutMaintenanceStartTimeOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutMaintenanceStartTimeOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_cbor(data: dict) -> PutMaintenanceStartTimeOutput:
    out: PutMaintenanceStartTimeOutput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    return out
