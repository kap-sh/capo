"""Generated from Smithy shape ``com.amazonaws.neptunegraph#RestoreGraphFromSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.replica_count
    import capo_neptune_graph.types.snapshot_identifier
    import capo_neptune_graph.types.tag_map


class RestoreGraphFromSnapshotInput(TypedDict, closed=True):
    snapshot_identifier: (
        "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier"
    )
    """<p>The ID of the snapshot in question.</p>"""
    graph_name: "capo_neptune_graph.types.graph_name.GraphName"
    """<p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    provisioned_memory: NotRequired[
        "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>"""
    tags: NotRequired["capo_neptune_graph.types.tag_map.TagMap"]
    """<p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>"""
    replica_count: NotRequired["capo_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>"""
    public_connectivity: NotRequired["bool"]
    """<p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreGraphFromSnapshotInput) -> dict:
    out: dict = {}
    out["graphName"] = value["graph_name"]
    if "provisioned_memory" in value:
        out["provisionedMemory"] = value["provisioned_memory"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "tags" in value:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.serialize_json(value["tags"])
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    return out


def deserialize_json(data: dict) -> RestoreGraphFromSnapshotInput:
    out: RestoreGraphFromSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("graphName") is not None:
        out["graph_name"] = data["graphName"]
    else:
        out["graph_name"] = ""
    if data.get("provisionedMemory") is not None:
        out["provisioned_memory"] = data["provisionedMemory"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("tags") is not None:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    if data.get("replicaCount") is not None:
        out["replica_count"] = data["replicaCount"]
    if data.get("publicConnectivity") is not None:
        out["public_connectivity"] = data["publicConnectivity"]
    return out
