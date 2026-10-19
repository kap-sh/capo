"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListPrivateGraphEndpointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.pagination_token
    import capo_neptune_graph.types.private_graph_endpoint_summary_list


class ListPrivateGraphEndpointsOutput(TypedDict, closed=True):
    private_graph_endpoints: "capo_neptune_graph.types.private_graph_endpoint_summary_list.PrivateGraphEndpointSummaryList"
    """<p>A list of private endpoints for the specified Neptune Analytics graph.</p>"""
    next_token: NotRequired["capo_neptune_graph.types.pagination_token.PaginationToken"]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateGraphEndpointsOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.private_graph_endpoint_summary_list

    out["privateGraphEndpoints"] = (
        capo_neptune_graph.types.private_graph_endpoint_summary_list.serialize_json(
            value["private_graph_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivateGraphEndpointsOutput:
    out: ListPrivateGraphEndpointsOutput = {}  # type: ignore[typeddict-item]
    if data.get("privateGraphEndpoints") is not None:
        import capo_neptune_graph.types.private_graph_endpoint_summary_list

        out["private_graph_endpoints"] = (
            capo_neptune_graph.types.private_graph_endpoint_summary_list.deserialize_json(
                data["privateGraphEndpoints"]
            )
        )
    else:
        out["private_graph_endpoints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
