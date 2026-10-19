"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetContextGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.edge_filters
    import capo_cloudwatchomni.types.node_filters
    import capo_cloudwatchomni.types.pagination_token


class GetContextGraphInput(TypedDict, closed=True):
    node_filters: NotRequired["capo_cloudwatchomni.types.node_filters.NodeFilters"]
    """Criteria restricting which nodes are returned."""
    edge_filters: NotRequired["capo_cloudwatchomni.types.edge_filters.EdgeFilters"]
    """Criteria restricting which edges are returned."""
    start_time: "datetime.datetime"
    """Start of the time range (UTC), inclusive."""
    end_time: "datetime.datetime"
    """End of the time range (UTC), inclusive."""
    depth: NotRequired["int"]
    """How many hops to traverse out from the nodes matched by nodeFilters. 0 returns only the matched nodes themselves."""
    max_results: NotRequired["int"]
    """The maximum number of nodes to return in a single page."""
    max_edges_per_node: NotRequired["int"]
    """The maximum number of edges to return per node, bounding the fan-out of a densely connected node."""
    include_metadata: NotRequired["bool"]
    """Whether to return the metadata block, semantics included, on each node and edge. Off by default because it costs an extra lookup per returned node."""
    next_token: NotRequired[
        "capo_cloudwatchomni.types.pagination_token.PaginationToken"
    ]
    """Pagination token from a previous response, to retrieve the next page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetContextGraphInput) -> dict:
    out: dict = {}
    if "node_filters" in value:
        import capo_cloudwatchomni.types.node_filters

        out["nodeFilters"] = capo_cloudwatchomni.types.node_filters.serialize_cbor(
            value["node_filters"]
        )
    if "edge_filters" in value:
        import capo_cloudwatchomni.types.edge_filters

        out["edgeFilters"] = capo_cloudwatchomni.types.edge_filters.serialize_cbor(
            value["edge_filters"]
        )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["startTime"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["start_time"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["endTime"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["end_time"]
    )
    if "depth" in value:
        out["depth"] = value["depth"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "max_edges_per_node" in value:
        out["maxEdgesPerNode"] = value["max_edges_per_node"]
    if "include_metadata" in value:
        out["includeMetadata"] = value["include_metadata"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetContextGraphInput:
    out: GetContextGraphInput = {}  # type: ignore[typeddict-item]
    if data.get("nodeFilters") is not None:
        import capo_cloudwatchomni.types.node_filters

        out["node_filters"] = capo_cloudwatchomni.types.node_filters.deserialize_cbor(
            data["nodeFilters"]
        )
    if data.get("edgeFilters") is not None:
        import capo_cloudwatchomni.types.edge_filters

        out["edge_filters"] = capo_cloudwatchomni.types.edge_filters.deserialize_cbor(
            data["edgeFilters"]
        )
    if data.get("startTime") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["start_time"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["end_time"] = capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("depth") is not None:
        out["depth"] = data["depth"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("maxEdgesPerNode") is not None:
        out["max_edges_per_node"] = data["maxEdgesPerNode"]
    if data.get("includeMetadata") is not None:
        out["include_metadata"] = data["includeMetadata"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
