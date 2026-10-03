"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRouteTableAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment
    import capo_networkmanager.types.peering_id
    import capo_networkmanager.types.transit_gateway_route_table_arn


class TransitGatewayRouteTableAttachment(TypedDict, closed=True):
    attachment: NotRequired["capo_networkmanager.types.attachment.Attachment"]
    peering_id: NotRequired["capo_networkmanager.types.peering_id.PeeringId"]
    """<p>The ID of the peering attachment.</p>"""
    transit_gateway_route_table_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn"
    ]
    """<p>The ARN of the transit gateway attachment route table. For example, <code>"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRouteTableAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_networkmanager.types.attachment

        out["Attachment"] = capo_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "peering_id" in value:
        out["PeeringId"] = value["peering_id"]
    if "transit_gateway_route_table_arn" in value:
        out["TransitGatewayRouteTableArn"] = value["transit_gateway_route_table_arn"]
    return out


def deserialize_json(data: dict) -> TransitGatewayRouteTableAttachment:
    out: TransitGatewayRouteTableAttachment = {}  # type: ignore[typeddict-item]
    if data.get("Attachment") is not None:
        import capo_networkmanager.types.attachment

        out["attachment"] = capo_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if data.get("PeeringId") is not None:
        out["peering_id"] = data["PeeringId"]
    if data.get("TransitGatewayRouteTableArn") is not None:
        out["transit_gateway_route_table_arn"] = data["TransitGatewayRouteTableArn"]
    return out
