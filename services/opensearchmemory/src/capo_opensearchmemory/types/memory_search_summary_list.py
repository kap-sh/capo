"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemorySearchSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_search_summary

MemorySearchSummaryList: TypeAlias = list[
    "capo_opensearchmemory.types.memory_search_summary.MemorySearchSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemorySearchSummaryList) -> list:
    import capo_opensearchmemory.types.memory_search_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.memory_search_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MemorySearchSummaryList:
    import capo_opensearchmemory.types.memory_search_summary

    out: MemorySearchSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.memory_search_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: MemorySearchSummaryList) -> list[Any]:
    import capo_opensearchmemory.types.memory_search_summary

    return [
        capo_opensearchmemory.types.memory_search_summary.redact_sensitive(item)
        for item in value
    ]
