"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetGenerationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_generation_summary

DatasetGenerationSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.dataset_generation_summary.DatasetGenerationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetGenerationSummaryList) -> list:
    import capo_bedrock_agentcore.types.dataset_generation_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.dataset_generation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DatasetGenerationSummaryList:
    import capo_bedrock_agentcore.types.dataset_generation_summary

    out: DatasetGenerationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.dataset_generation_summary.deserialize_json(
                item
            )
        )
    return out
