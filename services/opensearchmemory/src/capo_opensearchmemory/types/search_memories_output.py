"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SearchMemoriesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_search_summary_list
    import capo_opensearchmemory.types.pagination_token


class SearchMemoriesOutput(TypedDict, closed=True):
    memories: (
        "capo_opensearchmemory.types.memory_search_summary_list.MemorySearchSummaryList"
    )
    """<p>The matching memories, in the order <code>sort</code> requests, or most relevant first when it has none. Empty when nothing matches.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Absent when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchMemoriesOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory_search_summary_list

    out["memories"] = (
        capo_opensearchmemory.types.memory_search_summary_list.serialize_aws_json_1_0(
            value["memories"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchMemoriesOutput:
    out: SearchMemoriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("memories") is not None:
        import capo_opensearchmemory.types.memory_search_summary_list

        out["memories"] = (
            capo_opensearchmemory.types.memory_search_summary_list.deserialize_aws_json_1_0(
                data["memories"]
            )
        )
    else:
        out["memories"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchMemoriesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memories" in value:
        import capo_opensearchmemory.types.memory_search_summary_list

        out["memories"] = (
            capo_opensearchmemory.types.memory_search_summary_list.redact_sensitive(
                value["memories"]
            )
        )
    return out
