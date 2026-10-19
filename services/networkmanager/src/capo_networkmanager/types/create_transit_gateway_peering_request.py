"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateTransitGatewayPeeringRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.tag_list
    import capo_networkmanager.types.transit_gateway_arn


class CreateTransitGatewayPeeringRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    transit_gateway_arn: (
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    )
    """<p>The ARN of the transit gateway for the peering request.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTransitGatewayPeeringRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["TransitGatewayArn"] = value["transit_gateway_arn"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTransitGatewayPeeringRequest:
    out: CreateTransitGatewayPeeringRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("TransitGatewayArn") is not None:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    else:
        out["transit_gateway_arn"] = ""
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
