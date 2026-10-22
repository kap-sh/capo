"""Generated from Smithy shape ``com.amazonaws.rds#AvailableCapacityPerAvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class AvailableCapacityPerAvailabilityZone(TypedDict, closed=True):
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Availability Zone.</p>"""
    available_capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The number of DB instances that remain available in this Availability Zone. Amazon RDS decreases this value when a DB instance takes a unit of reserved capacity in this Availability Zone, and it increases this value when a DB instance releases that unit.</p> <p>A DB instance with a pending modification also holds a unit of reserved capacity. A DB instance has a pending modification when Amazon RDS accepts a change to the DB instance and applies that change later, during the maintenance window. Amazon RDS holds the unit from the time that it accepts the request. To find a DB instance with a pending modification, check <code>PendingModifiedValues</code> in the response of <code>DescribeDBInstances</code>.</p> <p>Amazon RDS reports available capacity only for a reservation that is in the <code>active</code> state and not past its end date. Otherwise, this value is <code>0</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableCapacityPerAvailabilityZone,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "available_capacity" in value:
        pairs.append(
            (f"{key_prefix}AvailableCapacity", str(value["available_capacity"]))
        )


def deserialize_query(el: Element) -> AvailableCapacityPerAvailabilityZone:
    out: AvailableCapacityPerAvailabilityZone = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_available_capacity = el.find("AvailableCapacity")
    if child_available_capacity is not None:
        out["available_capacity"] = int(child_available_capacity.text or "")
    return out
