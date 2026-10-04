"""Generated from Smithy shape ``com.amazonaws.connect#ConnectionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.connection_type

ConnectionTypeList: TypeAlias = list[
    "capo_connect.types.connection_type.ConnectionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionTypeList) -> list:
    import capo_connect.types.connection_type

    out: list = []
    for item in value:
        out.append(capo_connect.types.connection_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectionTypeList:
    import capo_connect.types.connection_type

    out: ConnectionTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.connection_type.deserialize_json(item))
    return out
