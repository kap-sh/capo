"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListMemoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_list_summary_list
    import capo_opensearchmemory.types.pagination_token


class ListMemoriesOutput(TypedDict, closed=True):
    memories: (
        "capo_opensearchmemory.types.memory_list_summary_list.MemoryListSummaryList"
    )
    """<p>The memories, in the requested order. Empty when there are none.</p>"""
    next_token: NotRequired[
        "capo_opensearchmemory.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Absent when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMemoriesOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory_list_summary_list

    out["memories"] = (
        capo_opensearchmemory.types.memory_list_summary_list.serialize_aws_json_1_0(
            value["memories"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMemoriesOutput:
    out: ListMemoriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("memories") is not None:
        import capo_opensearchmemory.types.memory_list_summary_list

        out["memories"] = (
            capo_opensearchmemory.types.memory_list_summary_list.deserialize_aws_json_1_0(
                data["memories"]
            )
        )
    else:
        out["memories"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
