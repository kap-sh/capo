"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_id


class NatGatewayMapping(TypedDict, closed=True):
    nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>A unique identifier for the NAT gateway to use with proxy resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayMapping) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NatGatewayMapping:
    out: NatGatewayMapping = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        out["nat_gateway_id"] = ""
    return out
