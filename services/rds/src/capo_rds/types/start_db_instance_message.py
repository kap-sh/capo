"""Generated from Smithy shape ``com.amazonaws.rds#StartDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation_identifier
    import capo_rds.types.string


class StartDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied instance identifier.</p>"""
    db_capacity_reservation_identifier: NotRequired[
        "capo_rds.types.db_capacity_reservation_identifier.DBCapacityReservationIdentifier"
    ]
    """<p>The identifier or the name of the DB capacity reservation for the DB instance to use after it starts. You can specify the identifier, which has the prefix <code>dbcr-</code>, or the reservation name.</p> <p>Specify this parameter when the DB instance stopped using a reservation, or when you want the DB instance to use a different reservation.</p> <p>If you omit this parameter, and the DB instance kept a DB capacity reservation when it stopped, Amazon RDS starts the DB instance in that reservation.</p> <p>If that reservation is deleted, ended, or cancelled, the DB instance still starts. Amazon RDS starts the DB instance outside the reservation, on unreserved capacity, and it charges on-demand prices for the DB instance.</p> <p>If that reservation has no available capacity in the Availability Zone of the DB instance, the request fails. Amazon RDS doesn't start the DB instance, and it doesn't wait for capacity in that Availability Zone. Specify a reservation that has available capacity in that Availability Zone, or retry the request after the reservation has available capacity.</p> <p>Constraints:</p> <ul> <li> <p>The reservation must be in the <code>active</code> state.</p> </li> <li> <p>The reservation must reserve capacity for the DB instance class and the engine of the DB instance.</p> </li> <li> <p>The reservation must cover the Availability Zone of the DB instance, and it must have available capacity in that Availability Zone.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_capacity_reservation_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationIdentifier",
                str(value["db_capacity_reservation_identifier"]),
            )
        )


def deserialize_query(el: Element) -> StartDBInstanceMessage:
    out: StartDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_capacity_reservation_identifier = el.find(
        "DBCapacityReservationIdentifier"
    )
    if child_db_capacity_reservation_identifier is not None:
        out["db_capacity_reservation_identifier"] = str(
            child_db_capacity_reservation_identifier.text or ""
        )
    return out
