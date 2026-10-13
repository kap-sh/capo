"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordsCreateInputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_create_input

MemoryRecordsCreateInputList: TypeAlias = list[
    "capo_bedrock_agentcore.types.memory_record_create_input.MemoryRecordCreateInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordsCreateInputList) -> list:
    import capo_bedrock_agentcore.types.memory_record_create_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.memory_record_create_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryRecordsCreateInputList:
    import capo_bedrock_agentcore.types.memory_record_create_input

    out: MemoryRecordsCreateInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.memory_record_create_input.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MemoryRecordsCreateInputList) -> list[Any]:
    import capo_bedrock_agentcore.types.memory_record_create_input

    return [
        capo_bedrock_agentcore.types.memory_record_create_input.redact_sensitive(item)
        for item in value
    ]
