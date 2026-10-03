"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.capacity_reservation_instance_platform
    import capo_ec2.types.double
    import capo_ec2.types.double_with_constraints
    import capo_ec2.types.instance_type
    import capo_ec2.types.integer
    import capo_ec2.types.integer_with_constraints
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class FleetCapacityReservation(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Capacity Reservation reserves capacity.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type for which the Capacity Reservation reserves capacity.</p>"""
    instance_platform: NotRequired[
        "capo_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation reserves capacity.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the Capacity Reservation reserves capacity.</p>"""
    total_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of instances for which the Capacity Reservation reserves capacity.</p>"""
    fulfilled_capacity: NotRequired["capo_ec2.types.double.Double"]
    """<p>The number of capacity units fulfilled by the Capacity Reservation. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation reserves capacity for EBS-optimized instance types.</p>"""
    create_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation was created.</p>"""
    weight: NotRequired["capo_ec2.types.double_with_constraints.DoubleWithConstraints"]
    """<p>The weight of the instance type in the Capacity Reservation Fleet. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-weight">Instance type weight</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    priority: NotRequired[
        "capo_ec2.types.integer_with_constraints.IntegerWithConstraints"
    ]
    """<p>The priority of the instance type in the Capacity Reservation Fleet. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-priority">Instance type priority</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetCapacityReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "instance_platform" in value:
        import capo_ec2.types.capacity_reservation_instance_platform

        capo_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{key_prefix}InstancePlatform"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "total_instance_count" in value:
        pairs.append(
            (f"{key_prefix}TotalInstanceCount", str(value["total_instance_count"]))
        )
    if "fulfilled_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}FulfilledCapacity",
                (
                    "NaN"
                    if value["fulfilled_capacity"] != value["fulfilled_capacity"]
                    else "Infinity"
                    if value["fulfilled_capacity"] == float("inf")
                    else "-Infinity"
                    if value["fulfilled_capacity"] == float("-inf")
                    else str(value["fulfilled_capacity"])
                ),
            )
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "create_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "weight" in value:
        pairs.append(
            (
                f"{key_prefix}Weight",
                (
                    "NaN"
                    if value["weight"] != value["weight"]
                    else "Infinity"
                    if value["weight"] == float("inf")
                    else "-Infinity"
                    if value["weight"] == float("-inf")
                    else str(value["weight"])
                ),
            )
        )
    if "priority" in value:
        pairs.append((f"{key_prefix}Priority", str(value["priority"])))


def deserialize_ec2_query(el: Element) -> FleetCapacityReservation:
    out: FleetCapacityReservation = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("capacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_instance_platform = el.find("instancePlatform")
    if child_instance_platform is not None:
        import capo_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            capo_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_total_instance_count = el.find("totalInstanceCount")
    if child_total_instance_count is not None:
        out["total_instance_count"] = int(child_total_instance_count.text or "")
    child_fulfilled_capacity = el.find("fulfilledCapacity")
    if child_fulfilled_capacity is not None:
        out["fulfilled_capacity"] = float(child_fulfilled_capacity.text or "")
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_create_date = el.find("createDate")
    if child_create_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_date
        )
    child_weight = el.find("weight")
    if child_weight is not None:
        out["weight"] = float(child_weight.text or "")
    child_priority = el.find("priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
