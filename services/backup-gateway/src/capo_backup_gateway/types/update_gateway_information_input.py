"""Generated from Smithy shape ``com.amazonaws.backupgateway#UpdateGatewayInformationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.name


class UpdateGatewayInformationInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway to update.</p>"""
    gateway_display_name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The updated display name of the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGatewayInformationInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    if "gateway_display_name" in value:
        out["GatewayDisplayName"] = value["gateway_display_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGatewayInformationInput:
    out: UpdateGatewayInformationInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        out["gateway_arn"] = ""
    if data.get("GatewayDisplayName") is not None:
        out["gateway_display_name"] = data["GatewayDisplayName"]
    return out
