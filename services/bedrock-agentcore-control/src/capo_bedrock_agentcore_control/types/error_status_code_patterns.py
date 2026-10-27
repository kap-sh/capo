"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ErrorStatusCodePatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.error_status_code_pattern

ErrorStatusCodePatterns: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.error_status_code_pattern.ErrorStatusCodePattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorStatusCodePatterns) -> list:
    return list(value)


def deserialize_json(data: list) -> ErrorStatusCodePatterns:
    return [item for item in data if item is not None]
