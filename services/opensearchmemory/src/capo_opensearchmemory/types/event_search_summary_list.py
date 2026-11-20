"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventSearchSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_search_summary

EventSearchSummaryList: TypeAlias = list[
    "capo_opensearchmemory.types.event_search_summary.EventSearchSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSearchSummaryList) -> list:
    import capo_opensearchmemory.types.event_search_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.event_search_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EventSearchSummaryList:
    import capo_opensearchmemory.types.event_search_summary

    out: EventSearchSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.event_search_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EventSearchSummaryList) -> list[Any]:
    import capo_opensearchmemory.types.event_search_summary

    return [
        capo_opensearchmemory.types.event_search_summary.redact_sensitive(item)
        for item in value
    ]
