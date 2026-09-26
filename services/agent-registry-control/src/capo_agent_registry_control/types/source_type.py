"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "AWS::BedrockAgentCore::Runtime",
    "AWS::BedrockAgentCore::Gateway",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    return cast(SourceType, data)
