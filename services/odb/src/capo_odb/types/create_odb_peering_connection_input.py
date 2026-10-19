"""Generated from Smithy shape ``com.amazonaws.odb#CreateOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.general_input_string
    import capo_odb.types.peer_network_route_table_id_list
    import capo_odb.types.peered_cidr_list
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn


class CreateOdbPeeringConnectionInput(TypedDict, closed=True):
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network that initiates the peering connection.</p>"""
    peer_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The display name for the ODB peering connection.</p>"""
    peer_network_cidrs_to_be_added: NotRequired[
        "capo_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>"""
    peer_network_route_table_ids: NotRequired[
        "capo_odb.types.peer_network_route_table_id_list.PeerNetworkRouteTableIdList"
    ]
    """<p>The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>The client token for the ODB peering connection request.</p> <p>Constraints:</p> <ul> <li> <p>Must be unique for each request.</p> </li> </ul>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The tags to assign to the ODB peering connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    out["odbNetworkId"] = value["odb_network_id"]
    out["peerNetworkId"] = value["peer_network_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peer_network_cidrs_to_be_added" in value:
        import capo_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeAdded"] = (
            capo_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_added"]
            )
        )
    if "peer_network_route_table_ids" in value:
        import capo_odb.types.peer_network_route_table_id_list

        out["peerNetworkRouteTableIds"] = (
            capo_odb.types.peer_network_route_table_id_list.serialize_aws_json_1_0(
                value["peer_network_route_table_ids"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOdbPeeringConnectionInput:
    out: CreateOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    if data.get("peerNetworkId") is not None:
        out["peer_network_id"] = data["peerNetworkId"]
    else:
        out["peer_network_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("peerNetworkCidrsToBeAdded") is not None:
        import capo_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_added"] = (
            capo_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeAdded"]
            )
        )
    if data.get("peerNetworkRouteTableIds") is not None:
        import capo_odb.types.peer_network_route_table_id_list

        out["peer_network_route_table_ids"] = (
            capo_odb.types.peer_network_route_table_id_list.deserialize_aws_json_1_0(
                data["peerNetworkRouteTableIds"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
