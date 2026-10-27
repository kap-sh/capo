"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FallbackErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.fallback_error

FallbackErrors: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.fallback_error.FallbackError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FallbackErrors) -> list:
    import capo_bedrock_agentcore_control.types.fallback_error

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.fallback_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FallbackErrors:
    import capo_bedrock_agentcore_control.types.fallback_error

    out: FallbackErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.fallback_error.deserialize_json(item)
        )
    return out
