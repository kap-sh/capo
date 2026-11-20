"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_summary

EventSummaryList: TypeAlias = list[
    "capo_opensearchmemory.types.event_summary.EventSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSummaryList) -> list:
    import capo_opensearchmemory.types.event_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.event_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EventSummaryList:
    import capo_opensearchmemory.types.event_summary

    out: EventSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.event_summary.deserialize_aws_json_1_0(item)
        )
    return out
