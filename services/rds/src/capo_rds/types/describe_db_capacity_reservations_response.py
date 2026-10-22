"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBCapacityReservationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation_list
    import capo_rds.types.string


class DescribeDBCapacityReservationsResponse(TypedDict, closed=True):
    db_capacity_reservations: NotRequired[
        "capo_rds.types.db_capacity_reservation_list.DBCapacityReservationList"
    ]
    """<p>A list of DB capacity reservations.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>A pagination token that you can use in a later <code>DescribeDBCapacityReservations</code> request. If this value is returned, more records are available beyond this response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBCapacityReservationsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservations" in value:
        import capo_rds.types.db_capacity_reservation_list

        capo_rds.types.db_capacity_reservation_list.serialize_query(
            value["db_capacity_reservations"],
            pairs,
            f"{key_prefix}DBCapacityReservations",
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBCapacityReservationsResponse:
    out: DescribeDBCapacityReservationsResponse = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservations = el.find("DBCapacityReservations")
    if child_db_capacity_reservations is not None:
        import capo_rds.types.db_capacity_reservation_list

        out["db_capacity_reservations"] = (
            capo_rds.types.db_capacity_reservation_list.deserialize_query(
                child_db_capacity_reservations
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
