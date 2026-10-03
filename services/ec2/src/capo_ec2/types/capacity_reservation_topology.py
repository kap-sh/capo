"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTopology``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_node_set
    import capo_ec2.types.string


class CapacityReservationTopology(TypedDict, closed=True):
    capacity_reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    capacity_block_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Block. This parameter is only supported for UltraServer instances and identifies instances within the UltraServer domain.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the Capacity Reservation. For the list of possible states, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html">DescribeCapacityReservations</a>.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the placement group that the Capacity Reservation is in.</p>"""
    network_nodes: NotRequired["capo_ec2.types.network_node_set.NetworkNodeSet"]
    """<p>The network nodes. The nodes are hashed based on your account. Capacity Reservations from different accounts running under the same server will return a different hashed list of strings.</p> <p>The value is <code>null</code> or empty if:</p> <ul> <li> <p>The instance type is not supported.</p> </li> <li> <p>The Capacity Reservation is in a state other than <code>active</code> or <code>pending</code>.</p> </li> </ul>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone that the Capacity Reservation is in.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Availability Zone or Local Zone that the Capacity Reservation is in.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationTopology, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "capacity_block_id" in value:
        pairs.append((f"{key_prefix}CapacityBlockId", str(value["capacity_block_id"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "network_nodes" in value:
        import capo_ec2.types.network_node_set

        capo_ec2.types.network_node_set.serialize_ec2_query(
            value["network_nodes"], pairs, f"{key_prefix}NetworkNodeSet"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))


def deserialize_ec2_query(el: Element) -> CapacityReservationTopology:
    out: CapacityReservationTopology = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("capacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_capacity_block_id = el.find("capacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_network_nodes = el.find("networkNodeSet")
    if child_network_nodes is not None:
        import capo_ec2.types.network_node_set

        out["network_nodes"] = capo_ec2.types.network_node_set.deserialize_ec2_query(
            child_network_nodes
        )
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    return out
