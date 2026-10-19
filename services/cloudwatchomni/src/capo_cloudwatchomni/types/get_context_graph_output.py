"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetContextGraphOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.node_list
    import capo_cloudwatchomni.types.pagination_token


class GetContextGraphOutput(TypedDict, closed=True):
    nodes: "capo_cloudwatchomni.types.node_list.NodeList"
    """The page of nodes matching the request. This is the paginated collection."""
    next_token: NotRequired[
        "capo_cloudwatchomni.types.pagination_token.PaginationToken"
    ]
    """Pagination token for the next page; absent when there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetContextGraphOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.node_list

    out["nodes"] = capo_cloudwatchomni.types.node_list.serialize_cbor(value["nodes"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetContextGraphOutput:
    out: GetContextGraphOutput = {}  # type: ignore[typeddict-item]
    if data.get("nodes") is not None:
        import capo_cloudwatchomni.types.node_list

        out["nodes"] = capo_cloudwatchomni.types.node_list.deserialize_cbor(
            data["nodes"]
        )
    else:
        out["nodes"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
