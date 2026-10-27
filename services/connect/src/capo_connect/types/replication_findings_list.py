"""Generated from Smithy shape ``com.amazonaws.connect#ReplicationFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.replication_finding

ReplicationFindingsList: TypeAlias = list[
    "capo_connect.types.replication_finding.ReplicationFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationFindingsList) -> list:
    import capo_connect.types.replication_finding

    out: list = []
    for item in value:
        out.append(capo_connect.types.replication_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReplicationFindingsList:
    import capo_connect.types.replication_finding

    out: ReplicationFindingsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.replication_finding.deserialize_json(item))
    return out
