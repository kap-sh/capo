"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetGenerationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_generation_id

DatasetGenerationIdList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.dataset_generation_id.DatasetGenerationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetGenerationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DatasetGenerationIdList:
    return [item for item in data if item is not None]
