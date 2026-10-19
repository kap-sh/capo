"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListGraphSnapshotsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_snapshot_summary_list
    import capo_neptune_graph.types.pagination_token


class ListGraphSnapshotsOutput(TypedDict, closed=True):
    graph_snapshots: (
        "capo_neptune_graph.types.graph_snapshot_summary_list.GraphSnapshotSummaryList"
    )
    """<p>The requested list of snapshots.</p>"""
    next_token: NotRequired["capo_neptune_graph.types.pagination_token.PaginationToken"]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphSnapshotsOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.graph_snapshot_summary_list

    out["graphSnapshots"] = (
        capo_neptune_graph.types.graph_snapshot_summary_list.serialize_json(
            value["graph_snapshots"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphSnapshotsOutput:
    out: ListGraphSnapshotsOutput = {}  # type: ignore[typeddict-item]
    if data.get("graphSnapshots") is not None:
        import capo_neptune_graph.types.graph_snapshot_summary_list

        out["graph_snapshots"] = (
            capo_neptune_graph.types.graph_snapshot_summary_list.deserialize_json(
                data["graphSnapshots"]
            )
        )
    else:
        out["graph_snapshots"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
