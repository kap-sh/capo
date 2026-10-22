"""Generated from Smithy shape ``com.amazonaws.rds#DBCapacityReservationState``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

DBCapacityReservationState: TypeAlias = Literal[
    "active",
    "expired",
    "cancelled",
    "pending",
    "failed",
    "assessing",
    "scheduled",
    "delayed",
    "unsupported",
]


# --- awsQuery ser/de ---
def to_query_text(value: DBCapacityReservationState) -> str:
    return value


def from_query_text(text: str) -> DBCapacityReservationState:
    return cast(DBCapacityReservationState, text)


def serialize_query(
    value: DBCapacityReservationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DBCapacityReservationState:
    return from_query_text(el.text or "")
