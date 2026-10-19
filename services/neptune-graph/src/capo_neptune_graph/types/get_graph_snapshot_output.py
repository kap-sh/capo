"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.snapshot_id
    import capo_neptune_graph.types.snapshot_name
    import capo_neptune_graph.types.snapshot_status


class GetGraphSnapshotOutput(TypedDict, closed=True):
    id: "capo_neptune_graph.types.snapshot_id.SnapshotId"
    """<p>The unique identifier of the graph snapshot.</p>"""
    name: "capo_neptune_graph.types.snapshot_name.SnapshotName"
    """<p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    arn: "str"
    """<p>The ARN of the graph snapshot.</p>"""
    source_graph_id: NotRequired["capo_neptune_graph.types.graph_id.GraphId"]
    """<p>The graph identifier for the graph for which a snapshot is to be created.</p>"""
    snapshot_create_time: NotRequired["datetime.datetime"]
    """<p>The time when the snapshot was created.</p>"""
    status: NotRequired["capo_neptune_graph.types.snapshot_status.SnapshotStatus"]
    """<p>The status of the graph snapshot.</p>"""
    kms_key_identifier: NotRequired["capo_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>The ID of the KMS key used to encrypt and decrypt the snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSnapshotOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "source_graph_id" in value:
        out["sourceGraphId"] = value["source_graph_id"]
    if "snapshot_create_time" in value:
        import capo_neptune_graph.types._prelude.timestamp

        out["snapshotCreateTime"] = (
            capo_neptune_graph.types._prelude.timestamp.serialize_json(
                value["snapshot_create_time"]
            )
        )
    if "status" in value:
        import capo_neptune_graph.types.snapshot_status

        out["status"] = capo_neptune_graph.types.snapshot_status.serialize_json(
            value["status"]
        )
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> GetGraphSnapshotOutput:
    out: GetGraphSnapshotOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("sourceGraphId") is not None:
        out["source_graph_id"] = data["sourceGraphId"]
    if data.get("snapshotCreateTime") is not None:
        import capo_neptune_graph.types._prelude.timestamp

        out["snapshot_create_time"] = (
            capo_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["snapshotCreateTime"]
            )
        )
    if data.get("status") is not None:
        import capo_neptune_graph.types.snapshot_status

        out["status"] = capo_neptune_graph.types.snapshot_status.deserialize_json(
            data["status"]
        )
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    return out
