"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateTransitGatewayRouteTableAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.peering_id
    import capo_networkmanager.types.tag_list
    import capo_networkmanager.types.transit_gateway_route_table_arn


class CreateTransitGatewayRouteTableAttachmentRequest(TypedDict, closed=True):
    peering_id: "capo_networkmanager.types.peering_id.PeeringId"
    """<p>The ID of the peer for the </p>"""
    transit_gateway_route_table_arn: "capo_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn"
    """<p>The ARN of the transit gateway route table for the attachment request. For example, <code>"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"</code>.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Transit Gateway route table attachment for traffic routing decisions.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTransitGatewayRouteTableAttachmentRequest) -> dict:
    out: dict = {}
    out["PeeringId"] = value["peering_id"]
    out["TransitGatewayRouteTableArn"] = value["transit_gateway_route_table_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTransitGatewayRouteTableAttachmentRequest:
    out: CreateTransitGatewayRouteTableAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("PeeringId") is not None:
        out["peering_id"] = data["PeeringId"]
    else:
        raise DeserializationError(
            "CreateTransitGatewayRouteTableAttachmentRequest.peering_id required"
        )
    if data.get("TransitGatewayRouteTableArn") is not None:
        out["transit_gateway_route_table_arn"] = data["TransitGatewayRouteTableArn"]
    else:
        raise DeserializationError(
            "CreateTransitGatewayRouteTableAttachmentRequest.transit_gateway_route_table_arn required"
        )
    if data.get("RoutingPolicyLabel") is not None:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
