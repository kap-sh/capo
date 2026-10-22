"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation_identifier
    import capo_rds.types.end_date_type
    import capo_rds.types.integer_optional
    import capo_rds.types.t_stamp


class ModifyDBCapacityReservationRequest(TypedDict, closed=True):
    db_capacity_reservation_identifier: NotRequired[
        "capo_rds.types.db_capacity_reservation_identifier.DBCapacityReservationIdentifier"
    ]
    """<p>The identifier or the name of the DB capacity reservation to modify. You can specify the identifier, which has the prefix <code>dbcr-</code>, or the reservation name.</p>"""
    capacity_per_availability_zone: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The new number of DB instances to reserve in each Availability Zone of the reservation. Amazon RDS applies this number to every Availability Zone of the reservation.</p> <p>An increase reserves more capacity at the time of the request, so it can fail when the Amazon Web Services Region has insufficient capacity.</p> <p>This value multiplied by the number of Availability Zones counts against the DB instances quota for your Amazon Web Services account in the Amazon Web Services Region. Amazon RDS checks the quota only when you increase the value.</p> <p>Constraints:</p> <ul> <li> <p>Minimum 1.</p> </li> <li> <p>Can't be less than the highest number of DB instances that use the reservation in any single Availability Zone of the reservation. That number includes a DB instance that holds a unit of reserved capacity for a pending modification. To find that number for an Availability Zone, subtract <code>AvailableCapacity</code> from <code>ReservedCapacityPerAvailabilityZone</code>.</p> </li> <li> <p>During a capacity commitment, can't be less than <code>CommittedCapacityPerAvailabilityZone</code>.</p> </li> </ul>"""
    end_date_type: NotRequired["capo_rds.types.end_date_type.EndDateType"]
    """<p>The end date type for the reservation.</p> <p>Valid Values:</p> <ul> <li> <p> <code>limited</code> - The reservation has a specific end date. You must also specify <code>EndDate</code>.</p> </li> <li> <p> <code>unlimited</code> - The reservation doesn't expire. Don't specify <code>EndDate</code>.</p> </li> </ul>"""
    end_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The new end date for the reservation, in Universal Coordinated Time (UTC). Required when <code>EndDateType</code> is <code>limited</code>. Don't specify a value when <code>EndDateType</code> is <code>unlimited</code>.</p> <p>When you specify <code>EndDate</code>, you must also specify <code>EndDateType</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be a date and time in the future.</p> </li> <li> <p>During a capacity commitment, must be at or after <code>CommitmentEndDate</code>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservation_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationIdentifier",
                str(value["db_capacity_reservation_identifier"]),
            )
        )
    if "capacity_per_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityPerAvailabilityZone",
                str(value["capacity_per_availability_zone"]),
            )
        )
    if "end_date_type" in value:
        import capo_rds.types.end_date_type

        capo_rds.types.end_date_type.serialize_query(
            value["end_date_type"], pairs, f"{key_prefix}EndDateType"
        )
    if "end_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )


def deserialize_query(el: Element) -> ModifyDBCapacityReservationRequest:
    out: ModifyDBCapacityReservationRequest = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservation_identifier = el.find(
        "DBCapacityReservationIdentifier"
    )
    if child_db_capacity_reservation_identifier is not None:
        out["db_capacity_reservation_identifier"] = str(
            child_db_capacity_reservation_identifier.text or ""
        )
    child_capacity_per_availability_zone = el.find("CapacityPerAvailabilityZone")
    if child_capacity_per_availability_zone is not None:
        out["capacity_per_availability_zone"] = int(
            child_capacity_per_availability_zone.text or ""
        )
    child_end_date_type = el.find("EndDateType")
    if child_end_date_type is not None:
        import capo_rds.types.end_date_type

        out["end_date_type"] = capo_rds.types.end_date_type.deserialize_query(
            child_end_date_type
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_rds.types.t_stamp

        out["end_date"] = capo_rds.types.t_stamp.deserialize_query(child_end_date)
    return out
