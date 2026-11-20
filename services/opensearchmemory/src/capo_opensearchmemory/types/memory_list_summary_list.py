"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryListSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_list_summary

MemoryListSummaryList: TypeAlias = list[
    "capo_opensearchmemory.types.memory_list_summary.MemoryListSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryListSummaryList) -> list:
    import capo_opensearchmemory.types.memory_list_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.memory_list_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MemoryListSummaryList:
    import capo_opensearchmemory.types.memory_list_summary

    out: MemoryListSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.memory_list_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
