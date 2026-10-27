"""Generated from Smithy shape ``com.amazonaws.connect#ResourceReplicationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.resource_replication_status

ResourceReplicationStatuses: TypeAlias = list[
    "capo_connect.types.resource_replication_status.ResourceReplicationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceReplicationStatuses) -> list:
    import capo_connect.types.resource_replication_status

    out: list = []
    for item in value:
        out.append(capo_connect.types.resource_replication_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceReplicationStatuses:
    import capo_connect.types.resource_replication_status

    out: ResourceReplicationStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.resource_replication_status.deserialize_json(item)
        )
    return out
