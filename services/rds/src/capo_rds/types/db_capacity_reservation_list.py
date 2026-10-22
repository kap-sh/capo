"""Generated from Smithy shape ``com.amazonaws.rds#DBCapacityReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation

DBCapacityReservationList: TypeAlias = list[
    "capo_rds.types.db_capacity_reservation.DBCapacityReservation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBCapacityReservationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_capacity_reservation

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_capacity_reservation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DBCapacityReservationList:
    import capo_rds.types.db_capacity_reservation

    out: DBCapacityReservationList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.db_capacity_reservation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBCapacityReservationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_capacity_reservation

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_capacity_reservation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBCapacityReservationList:
    import capo_rds.types.db_capacity_reservation

    out: DBCapacityReservationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_capacity_reservation.deserialize_query(child))
    return out
