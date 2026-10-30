"""Generated from Smithy shape ``com.amazonaws.opensearch#ReplicationPeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.replication_peer

ReplicationPeerList: TypeAlias = list[
    "capo_opensearch.types.replication_peer.ReplicationPeer"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationPeerList) -> list:
    import capo_opensearch.types.replication_peer

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.replication_peer.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReplicationPeerList:
    import capo_opensearch.types.replication_peer

    out: ReplicationPeerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearch.types.replication_peer.deserialize_json(item))
    return out
