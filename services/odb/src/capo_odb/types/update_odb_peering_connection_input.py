"""Generated from Smithy shape ``com.amazonaws.odb#UpdateOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.peered_cidr_list
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn


class UpdateOdbPeeringConnectionInput(TypedDict, closed=True):
    odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The identifier of the Oracle Database@Amazon Web Services peering connection to update.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new display name for the peering connection.</p>"""
    peer_network_cidrs_to_be_added: NotRequired[
        "capo_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@Amazon Web Services network.</p>"""
    peer_network_cidrs_to_be_removed: NotRequired[
        "capo_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    out["odbPeeringConnectionId"] = value["odb_peering_connection_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peer_network_cidrs_to_be_added" in value:
        import capo_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeAdded"] = (
            capo_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_added"]
            )
        )
    if "peer_network_cidrs_to_be_removed" in value:
        import capo_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeRemoved"] = (
            capo_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_removed"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOdbPeeringConnectionInput:
    out: UpdateOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("odbPeeringConnectionId") is not None:
        out["odb_peering_connection_id"] = data["odbPeeringConnectionId"]
    else:
        out["odb_peering_connection_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("peerNetworkCidrsToBeAdded") is not None:
        import capo_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_added"] = (
            capo_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeAdded"]
            )
        )
    if data.get("peerNetworkCidrsToBeRemoved") is not None:
        import capo_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_removed"] = (
            capo_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeRemoved"]
            )
        )
    return out
