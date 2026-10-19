"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StartGraphOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.graph_status
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.replica_count
    import capo_neptune_graph.types.snapshot_id
    import capo_neptune_graph.types.vector_search_configuration


class StartGraphOutput(TypedDict, closed=True):
    id: "capo_neptune_graph.types.graph_id.GraphId"
    """<p>The unique identifier of the graph.</p>"""
    name: "capo_neptune_graph.types.graph_name.GraphName"
    """<p>The name of the graph.</p>"""
    arn: "str"
    """<p>The ARN associated with the graph.</p>"""
    status: NotRequired["capo_neptune_graph.types.graph_status.GraphStatus"]
    """<p>The status of the graph.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason that the graph has this status.</p>"""
    create_time: NotRequired["datetime.datetime"]
    """<p>The time at which the graph was created.</p>"""
    provisioned_memory: NotRequired[
        "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.</p>"""
    endpoint: NotRequired["str"]
    """<p>The graph endpoint.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>If <code>true</code>, the graph has a public endpoint, otherwise not.</p>"""
    vector_search_configuration: NotRequired[
        "capo_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
    ]
    replica_count: NotRequired["capo_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas for the graph.</p>"""
    kms_key_identifier: NotRequired["capo_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>The ID of the KMS key used to encrypt and decrypt graph data.</p>"""
    source_snapshot_id: NotRequired["capo_neptune_graph.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot from which the graph was created, if it was created from a snapshot.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>If <code>true</code>, deletion protection is enabled for the graph.</p>"""
    build_number: NotRequired["str"]
    """<p>The build number of the graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartGraphOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_neptune_graph.types.graph_status

        out["status"] = capo_neptune_graph.types.graph_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "create_time" in value:
        import capo_neptune_graph.types._prelude.timestamp

        out["createTime"] = capo_neptune_graph.types._prelude.timestamp.serialize_json(
            value["create_time"]
        )
    if "provisioned_memory" in value:
        out["provisionedMemory"] = value["provisioned_memory"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    if "vector_search_configuration" in value:
        import capo_neptune_graph.types.vector_search_configuration

        out["vectorSearchConfiguration"] = (
            capo_neptune_graph.types.vector_search_configuration.serialize_json(
                value["vector_search_configuration"]
            )
        )
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "source_snapshot_id" in value:
        out["sourceSnapshotId"] = value["source_snapshot_id"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "build_number" in value:
        out["buildNumber"] = value["build_number"]
    return out


def deserialize_json(data: dict) -> StartGraphOutput:
    out: StartGraphOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("createTime") is not None:
        import capo_neptune_graph.types._prelude.timestamp

        out["create_time"] = (
            capo_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    if data.get("provisionedMemory") is not None:
        out["provisioned_memory"] = data["provisionedMemory"]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("publicConnectivity") is not None:
        out["public_connectivity"] = data["publicConnectivity"]
    if data.get("vectorSearchConfiguration") is not None:
        import capo_neptune_graph.types.vector_search_configuration

        out["vector_search_configuration"] = (
            capo_neptune_graph.types.vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    if data.get("replicaCount") is not None:
        out["replica_count"] = data["replicaCount"]
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if data.get("sourceSnapshotId") is not None:
        out["source_snapshot_id"] = data["sourceSnapshotId"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("buildNumber") is not None:
        out["build_number"] = data["buildNumber"]
    return out
