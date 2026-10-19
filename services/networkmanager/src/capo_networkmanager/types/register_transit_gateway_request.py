"""Generated from Smithy shape ``com.amazonaws.networkmanager#RegisterTransitGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.transit_gateway_arn


class RegisterTransitGatewayRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_arn: (
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    )
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterTransitGatewayRequest) -> dict:
    out: dict = {}
    out["TransitGatewayArn"] = value["transit_gateway_arn"]
    return out


def deserialize_json(data: dict) -> RegisterTransitGatewayRequest:
    out: RegisterTransitGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayArn") is not None:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    else:
        out["transit_gateway_arn"] = ""
    return out
