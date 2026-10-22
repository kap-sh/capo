"""Generated from Smithy shape ``com.amazonaws.rds#CancelDBCapacityReservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation


class CancelDBCapacityReservationResponse(TypedDict, closed=True):
    db_capacity_reservation: NotRequired[
        "capo_rds.types.db_capacity_reservation.DBCapacityReservation"
    ]
    """<p>Contains the details of the canceled DB capacity reservation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelDBCapacityReservationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservation" in value:
        import capo_rds.types.db_capacity_reservation

        capo_rds.types.db_capacity_reservation.serialize_query(
            value["db_capacity_reservation"],
            pairs,
            f"{key_prefix}DBCapacityReservation",
        )


def deserialize_query(el: Element) -> CancelDBCapacityReservationResponse:
    out: CancelDBCapacityReservationResponse = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservation = el.find("DBCapacityReservation")
    if child_db_capacity_reservation is not None:
        import capo_rds.types.db_capacity_reservation

        out["db_capacity_reservation"] = (
            capo_rds.types.db_capacity_reservation.deserialize_query(
                child_db_capacity_reservation
            )
        )
    return out
