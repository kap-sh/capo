"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationErrorSessionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_id

GenerationErrorSessionIdList: TypeAlias = list[
    "capo_bedrock_agentcore.types.session_id.SessionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationErrorSessionIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GenerationErrorSessionIdList:
    return [item for item in data if item is not None]
