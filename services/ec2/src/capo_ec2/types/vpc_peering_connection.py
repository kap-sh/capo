"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.multipath_resilience_status
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_peering_connection_state_reason
    import capo_ec2.types.vpc_peering_connection_vpc_info


class VpcPeeringConnection(TypedDict, closed=True):
    accepter_vpc_info: NotRequired[
        "capo_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    expiration_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time that an unaccepted VPC peering connection will expire.</p>"""
    requester_vpc_info: NotRequired[
        "capo_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    status: NotRequired[
        "capo_ec2.types.vpc_peering_connection_state_reason.VpcPeeringConnectionStateReason"
    ]
    """<p>The status of the VPC peering connection.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    vpc_peering_connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection.</p>"""
    multipath_resilience_status: NotRequired[
        "capo_ec2.types.multipath_resilience_status.MultipathResilienceStatus"
    ]
    """<p>The multipath resilience status of the VPC peering connection. The possible values are:</p> <ul> <li> <p> <code>enabled</code> – Both the requester and the accepter allow multipath resilience.</p> </li> <li> <p> <code>pending</code> – Either the requester or the accepter allows multipath resilience, but not both.</p> </li> <li> <p> <code>disabled</code> – Neither the requester nor the accepter allows multipath resilience.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcPeeringConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "accepter_vpc_info" in value:
        import capo_ec2.types.vpc_peering_connection_vpc_info

        capo_ec2.types.vpc_peering_connection_vpc_info.serialize_ec2_query(
            value["accepter_vpc_info"], pairs, f"{key_prefix}AccepterVpcInfo"
        )
    if "expiration_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["expiration_time"], pairs, f"{key_prefix}ExpirationTime"
        )
    if "requester_vpc_info" in value:
        import capo_ec2.types.vpc_peering_connection_vpc_info

        capo_ec2.types.vpc_peering_connection_vpc_info.serialize_ec2_query(
            value["requester_vpc_info"], pairs, f"{key_prefix}RequesterVpcInfo"
        )
    if "status" in value:
        import capo_ec2.types.vpc_peering_connection_state_reason

        capo_ec2.types.vpc_peering_connection_state_reason.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "multipath_resilience_status" in value:
        import capo_ec2.types.multipath_resilience_status

        capo_ec2.types.multipath_resilience_status.serialize_ec2_query(
            value["multipath_resilience_status"],
            pairs,
            f"{key_prefix}MultipathResilienceStatus",
        )


def deserialize_ec2_query(el: Element) -> VpcPeeringConnection:
    out: VpcPeeringConnection = {}  # type: ignore[typeddict-item]
    child_accepter_vpc_info = el.find("accepterVpcInfo")
    if child_accepter_vpc_info is not None:
        import capo_ec2.types.vpc_peering_connection_vpc_info

        out["accepter_vpc_info"] = (
            capo_ec2.types.vpc_peering_connection_vpc_info.deserialize_ec2_query(
                child_accepter_vpc_info
            )
        )
    child_expiration_time = el.find("expirationTime")
    if child_expiration_time is not None:
        import capo_ec2.types.date_time

        out["expiration_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_expiration_time
        )
    child_requester_vpc_info = el.find("requesterVpcInfo")
    if child_requester_vpc_info is not None:
        import capo_ec2.types.vpc_peering_connection_vpc_info

        out["requester_vpc_info"] = (
            capo_ec2.types.vpc_peering_connection_vpc_info.deserialize_ec2_query(
                child_requester_vpc_info
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.vpc_peering_connection_state_reason

        out["status"] = (
            capo_ec2.types.vpc_peering_connection_state_reason.deserialize_ec2_query(
                child_status
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_vpc_peering_connection_id = el.find("vpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_multipath_resilience_status = el.find("multipathResilienceStatus")
    if child_multipath_resilience_status is not None:
        import capo_ec2.types.multipath_resilience_status

        out["multipath_resilience_status"] = (
            capo_ec2.types.multipath_resilience_status.deserialize_ec2_query(
                child_multipath_resilience_status
            )
        )
    return out
