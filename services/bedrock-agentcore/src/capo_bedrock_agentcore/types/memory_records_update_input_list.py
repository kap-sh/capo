"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordsUpdateInputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_update_input

MemoryRecordsUpdateInputList: TypeAlias = list[
    "capo_bedrock_agentcore.types.memory_record_update_input.MemoryRecordUpdateInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordsUpdateInputList) -> list:
    import capo_bedrock_agentcore.types.memory_record_update_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.memory_record_update_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryRecordsUpdateInputList:
    import capo_bedrock_agentcore.types.memory_record_update_input

    out: MemoryRecordsUpdateInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.memory_record_update_input.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MemoryRecordsUpdateInputList) -> list[Any]:
    import capo_bedrock_agentcore.types.memory_record_update_input

    return [
        capo_bedrock_agentcore.types.memory_record_update_input.redact_sensitive(item)
        for item in value
    ]
