"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListGraphsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.graph_summary_list
    import capo_neptune_graph.types.pagination_token


class ListGraphsOutput(TypedDict, closed=True):
    graphs: "capo_neptune_graph.types.graph_summary_list.GraphSummaryList"
    """<p>A list of the graphs.</p>"""
    next_token: NotRequired["capo_neptune_graph.types.pagination_token.PaginationToken"]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphsOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.graph_summary_list

    out["graphs"] = capo_neptune_graph.types.graph_summary_list.serialize_json(
        value["graphs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphsOutput:
    out: ListGraphsOutput = {}  # type: ignore[typeddict-item]
    if data.get("graphs") is not None:
        import capo_neptune_graph.types.graph_summary_list

        out["graphs"] = capo_neptune_graph.types.graph_summary_list.deserialize_json(
            data["graphs"]
        )
    else:
        out["graphs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
