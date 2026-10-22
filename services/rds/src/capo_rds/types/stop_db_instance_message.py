"""Generated from Smithy shape ``com.amazonaws.rds#StopDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class StopDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied instance identifier.</p>"""
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied instance identifier of the DB Snapshot created immediately before the DB instance is stopped.</p>"""
    detach_from_db_capacity_reservation: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance stops using its DB capacity reservation when the DB instance stops. When you specify <code>true</code>, the DB instance belongs to no reservation after it stops, and a later start launches it outside the reservation.</p> <p>By default, a stopped DB instance keeps its DB capacity reservation, and a later start returns the DB instance to the same reservation.</p> <p>Every stop releases the unit of reserved capacity that the DB instance holds, for either value of this parameter. Another DB instance can then use that capacity. This parameter controls the reservation that the DB instance belongs to, and it does not control the release of the capacity.</p> <p>If the DB instance uses no DB capacity reservation, this parameter has no effect.</p> <important> <p>Amazon RDS holds no capacity for a stopped DB instance. When the reservation has no available capacity in the Availability Zone of the DB instance, a later start waits for capacity in that Availability Zone. When the DB instance belongs to no reservation, a later start can fail because the Amazon Web Services Region has insufficient capacity for the DB instance class.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "detach_from_db_capacity_reservation" in value:
        pairs.append(
            (
                f"{key_prefix}DetachFromDBCapacityReservation",
                "true" if value["detach_from_db_capacity_reservation"] else "false",
            )
        )


def deserialize_query(el: Element) -> StopDBInstanceMessage:
    out: StopDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_detach_from_db_capacity_reservation = el.find(
        "DetachFromDBCapacityReservation"
    )
    if child_detach_from_db_capacity_reservation is not None:
        out["detach_from_db_capacity_reservation"] = (
            child_detach_from_db_capacity_reservation.text or ""
        ).lower() == "true"
    return out
