"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.fleet_capacity_reservation_tenancy
    import capo_ec2.types.fleet_instance_match_criteria
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.reservation_fleet_instance_specification_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateCapacityReservationFleetRequest(TypedDict, closed=True):
    allocation_strategy: NotRequired["capo_ec2.types.string.String"]
    """<p>The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the <code>prioritized</code> allocation strategy is supported. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy"> Allocation strategy</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid values: <code>prioritized</code> </p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensure Idempotency</a>.</p>"""
    instance_type_specifications: NotRequired[
        "capo_ec2.types.reservation_fleet_instance_specification_list.ReservationFleetInstanceSpecificationList"
    ]
    """<p>Information about the instance types for which to reserve the capacity.</p>"""
    tenancy: NotRequired[
        "capo_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation Fleet is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    total_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to <code>expired</code> and all of the Capacity Reservations in the Fleet expire.</p> <p>The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify <code>5/31/2019</code>, <code>13:30:55</code>, the Capacity Reservation Fleet is guaranteed to expire between <code>13:30:55</code> and <code>14:30:55</code> on <code>5/31/2019</code>. </p>"""
    instance_match_criteria: NotRequired[
        "capo_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.</p> <p>Currently, Capacity Reservation Fleets support <code>open</code> instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationFleetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_strategy" in value:
        pairs.append(
            (f"{key_prefix}AllocationStrategy", str(value["allocation_strategy"]))
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "instance_type_specifications" in value:
        import capo_ec2.types.reservation_fleet_instance_specification_list

        capo_ec2.types.reservation_fleet_instance_specification_list.serialize_ec2_query(
            value["instance_type_specifications"],
            pairs,
            f"{key_prefix}InstanceTypeSpecification",
        )
    if "tenancy" in value:
        import capo_ec2.types.fleet_capacity_reservation_tenancy

        capo_ec2.types.fleet_capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{key_prefix}Tenancy"
        )
    if "total_target_capacity" in value:
        pairs.append(
            (f"{key_prefix}TotalTargetCapacity", str(value["total_target_capacity"]))
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "instance_match_criteria" in value:
        import capo_ec2.types.fleet_instance_match_criteria

        capo_ec2.types.fleet_instance_match_criteria.serialize_ec2_query(
            value["instance_match_criteria"],
            pairs,
            f"{key_prefix}InstanceMatchCriteria",
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationFleetRequest:
    out: CreateCapacityReservationFleetRequest = {}  # type: ignore[typeddict-item]
    child_allocation_strategy = el.find("AllocationStrategy")
    if child_allocation_strategy is not None:
        out["allocation_strategy"] = str(child_allocation_strategy.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instance_type_specifications = el.find("InstanceTypeSpecification")
    if child_instance_type_specifications is not None:
        import capo_ec2.types.reservation_fleet_instance_specification_list

        out["instance_type_specifications"] = (
            capo_ec2.types.reservation_fleet_instance_specification_list.deserialize_ec2_query(
                child_instance_type_specifications
            )
        )
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.fleet_capacity_reservation_tenancy

        out["tenancy"] = (
            capo_ec2.types.fleet_capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_total_target_capacity = el.find("TotalTargetCapacity")
    if child_total_target_capacity is not None:
        out["total_target_capacity"] = int(child_total_target_capacity.text or "")
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_instance_match_criteria = el.find("InstanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import capo_ec2.types.fleet_instance_match_criteria

        out["instance_match_criteria"] = (
            capo_ec2.types.fleet_instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
