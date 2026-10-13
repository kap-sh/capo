"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_summary

MemoryRecordSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.memory_record_summary.MemoryRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSummaryList) -> list:
    import capo_bedrock_agentcore.types.memory_record_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.memory_record_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryRecordSummaryList:
    import capo_bedrock_agentcore.types.memory_record_summary

    out: MemoryRecordSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.memory_record_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: MemoryRecordSummaryList) -> list[Any]:
    import capo_bedrock_agentcore.types.memory_record_summary

    return [
        capo_bedrock_agentcore.types.memory_record_summary.redact_sensitive(item)
        for item in value
    ]
