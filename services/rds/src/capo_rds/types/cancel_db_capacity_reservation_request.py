"""Generated from Smithy shape ``com.amazonaws.rds#CancelDBCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation_identifier


class CancelDBCapacityReservationRequest(TypedDict, closed=True):
    db_capacity_reservation_identifier: NotRequired[
        "capo_rds.types.db_capacity_reservation_identifier.DBCapacityReservationIdentifier"
    ]
    """<p>The identifier or the name of the DB capacity reservation to cancel. You can specify the identifier, which has the prefix <code>dbcr-</code>, or the reservation name.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelDBCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservation_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationIdentifier",
                str(value["db_capacity_reservation_identifier"]),
            )
        )


def deserialize_query(el: Element) -> CancelDBCapacityReservationRequest:
    out: CancelDBCapacityReservationRequest = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservation_identifier = el.find(
        "DBCapacityReservationIdentifier"
    )
    if child_db_capacity_reservation_identifier is not None:
        out["db_capacity_reservation_identifier"] = str(
            child_db_capacity_reservation_identifier.text or ""
        )
    return out
