"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcPeeringConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_peering_connection_options_request
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.vpc_id


class CreateVpcPeeringConnectionRequest(TypedDict, closed=True):
    peer_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</p> <p>Default: The Region in which you make the request.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the peering connection.</p>"""
    requester_peering_connection_options: NotRequired[
        "capo_ec2.types.create_peering_connection_options_request.CreatePeeringConnectionOptionsRequest"
    ]
    """<p>The VPC peering connection options to apply to the requester VPC.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the requester VPC. You must specify this parameter in the request.</p>"""
    peer_vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</p>"""
    peer_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the accepter VPC.</p> <p>Default: Your Amazon Web Services account ID</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcPeeringConnectionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "peer_region" in value:
        pairs.append((f"{key_prefix}PeerRegion", str(value["peer_region"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "requester_peering_connection_options" in value:
        import capo_ec2.types.create_peering_connection_options_request

        capo_ec2.types.create_peering_connection_options_request.serialize_ec2_query(
            value["requester_peering_connection_options"],
            pairs,
            f"{key_prefix}RequesterPeeringConnectionOptions",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "peer_vpc_id" in value:
        pairs.append((f"{key_prefix}PeerVpcId", str(value["peer_vpc_id"])))
    if "peer_owner_id" in value:
        pairs.append((f"{key_prefix}PeerOwnerId", str(value["peer_owner_id"])))


def deserialize_ec2_query(el: Element) -> CreateVpcPeeringConnectionRequest:
    out: CreateVpcPeeringConnectionRequest = {}  # type: ignore[typeddict-item]
    child_peer_region = el.find("PeerRegion")
    if child_peer_region is not None:
        out["peer_region"] = str(child_peer_region.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_requester_peering_connection_options = el.find(
        "RequesterPeeringConnectionOptions"
    )
    if child_requester_peering_connection_options is not None:
        import capo_ec2.types.create_peering_connection_options_request

        out["requester_peering_connection_options"] = (
            capo_ec2.types.create_peering_connection_options_request.deserialize_ec2_query(
                child_requester_peering_connection_options
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_peer_vpc_id = el.find("peerVpcId")
    if child_peer_vpc_id is not None:
        out["peer_vpc_id"] = str(child_peer_vpc_id.text or "")
    child_peer_owner_id = el.find("peerOwnerId")
    if child_peer_owner_id is not None:
        out["peer_owner_id"] = str(child_peer_owner_id.text or "")
    return out
