"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.snapshot_name
    import capo_neptune_graph.types.tag_map


class CreateGraphSnapshotInput(TypedDict, closed=True):
    graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    snapshot_name: "capo_neptune_graph.types.snapshot_name.SnapshotName"
    """<p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    tags: NotRequired["capo_neptune_graph.types.tag_map.TagMap"]
    """<p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphSnapshotInput) -> dict:
    out: dict = {}
    out["graphIdentifier"] = value["graph_identifier"]
    out["snapshotName"] = value["snapshot_name"]
    if "tags" in value:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGraphSnapshotInput:
    out: CreateGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("graphIdentifier") is not None:
        out["graph_identifier"] = data["graphIdentifier"]
    else:
        out["graph_identifier"] = ""
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("tags") is not None:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    return out
