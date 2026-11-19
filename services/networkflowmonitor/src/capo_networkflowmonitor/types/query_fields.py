"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.query_field

QueryFields: TypeAlias = list["capo_networkflowmonitor.types.query_field.QueryField"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryFields) -> list:
    import capo_networkflowmonitor.types.query_field

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.query_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryFields:
    import capo_networkflowmonitor.types.query_field

    out: QueryFields = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkflowmonitor.types.query_field.deserialize_json(item))
    return out
