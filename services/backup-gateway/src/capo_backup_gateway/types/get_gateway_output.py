"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetGatewayOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_details


class GetGatewayOutput(TypedDict, closed=True):
    gateway: NotRequired["capo_backup_gateway.types.gateway_details.GatewayDetails"]
    """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetGatewayOutput) -> dict:
    out: dict = {}
    if "gateway" in value:
        import capo_backup_gateway.types.gateway_details

        out["Gateway"] = (
            capo_backup_gateway.types.gateway_details.serialize_aws_json_1_0(
                value["gateway"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetGatewayOutput:
    out: GetGatewayOutput = {}  # type: ignore[typeddict-item]
    if data.get("Gateway") is not None:
        import capo_backup_gateway.types.gateway_details

        out["gateway"] = (
            capo_backup_gateway.types.gateway_details.deserialize_aws_json_1_0(
                data["Gateway"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetGatewayOutput) -> dict:
    out: dict = {}
    if "gateway" in value:
        import capo_backup_gateway.types.gateway_details

        out["Gateway"] = capo_backup_gateway.types.gateway_details.serialize_cbor(
            value["gateway"]
        )
    return out


def deserialize_cbor(data: dict) -> GetGatewayOutput:
    out: GetGatewayOutput = {}  # type: ignore[typeddict-item]
    if data.get("Gateway") is not None:
        import capo_backup_gateway.types.gateway_details

        out["gateway"] = capo_backup_gateway.types.gateway_details.deserialize_cbor(
            data["Gateway"]
        )
    return out
