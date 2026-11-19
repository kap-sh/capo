"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationTraceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.trace_id

GenerationTraceIdList: TypeAlias = list["capo_bedrock_agentcore.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationTraceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GenerationTraceIdList:
    return [item for item in data if item is not None]
