"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.source_server

SourceServersList: TypeAlias = list["capo_mgn.types.source_server.SourceServer"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServersList) -> list:
    import capo_mgn.types.source_server

    out: list = []
    for item in value:
        out.append(capo_mgn.types.source_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceServersList:
    import capo_mgn.types.source_server

    out: SourceServersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.source_server.deserialize_json(item))
    return out


def redact_sensitive(value: SourceServersList) -> list[Any]:
    import capo_mgn.types.source_server

    return [capo_mgn.types.source_server.redact_sensitive(item) for item in value]
