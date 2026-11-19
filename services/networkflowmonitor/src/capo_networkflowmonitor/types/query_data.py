"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.query_row

QueryData: TypeAlias = list["capo_networkflowmonitor.types.query_row.QueryRow"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryData) -> list:
    import capo_networkflowmonitor.types.query_row

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.query_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryData:
    import capo_networkflowmonitor.types.query_row

    out: QueryData = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkflowmonitor.types.query_row.deserialize_json(item))
    return out
