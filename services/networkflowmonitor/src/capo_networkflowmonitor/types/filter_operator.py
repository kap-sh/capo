"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "IN",
    "CONTAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
