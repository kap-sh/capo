"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.graph_status
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.replica_count


class GraphSummary(TypedDict, closed=True):
    id: "capo_neptune_graph.types.graph_id.GraphId"
    """<p>The unique identifier of the graph.</p>"""
    name: "capo_neptune_graph.types.graph_name.GraphName"
    """<p>The name of the graph.</p>"""
    arn: "str"
    """<p>The ARN associated with the graph.</p>"""
    status: NotRequired["capo_neptune_graph.types.graph_status.GraphStatus"]
    """<p>The status of the graph.</p>"""
    provisioned_memory: NotRequired[
        "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>If <code>true</code>, the graph has a public endpoint, otherwise not.</p>"""
    endpoint: NotRequired["str"]
    """<p>The graph endpoint.</p>"""
    replica_count: NotRequired["capo_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas for the graph.</p>"""
    kms_key_identifier: NotRequired["str"]
    """<p>The ID of the KMS key used to encrypt and decrypt graph data.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>If <code>true</code>, deletion protection is enabled for the graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GraphSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_neptune_graph.types.graph_status

        out["status"] = capo_neptune_graph.types.graph_status.serialize_json(
            value["status"]
        )
    if "provisioned_memory" in value:
        out["provisionedMemory"] = value["provisioned_memory"]
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_json(data: dict) -> GraphSummary:
    out: GraphSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_neptune_graph.types.graph_status

        out["status"] = capo_neptune_graph.types.graph_status.deserialize_json(
            data["status"]
        )
    if data.get("provisionedMemory") is not None:
        out["provisioned_memory"] = data["provisionedMemory"]
    if data.get("publicConnectivity") is not None:
        out["public_connectivity"] = data["publicConnectivity"]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("replicaCount") is not None:
        out["replica_count"] = data["replicaCount"]
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    return out
