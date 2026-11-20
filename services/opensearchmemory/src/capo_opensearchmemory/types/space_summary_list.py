"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SpaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_summary

SpaceSummaryList: TypeAlias = list[
    "capo_opensearchmemory.types.space_summary.SpaceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpaceSummaryList) -> list:
    import capo_opensearchmemory.types.space_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchmemory.types.space_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SpaceSummaryList:
    import capo_opensearchmemory.types.space_summary

    out: SpaceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchmemory.types.space_summary.deserialize_aws_json_1_0(item)
        )
    return out
