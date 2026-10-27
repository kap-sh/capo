"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetFallbacks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.fallback_target

TargetFallbacks: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.fallback_target.FallbackTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetFallbacks) -> list:
    import capo_bedrock_agentcore_control.types.fallback_target

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.fallback_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetFallbacks:
    import capo_bedrock_agentcore_control.types.fallback_target

    out: TargetFallbacks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.fallback_target.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TargetFallbacks) -> list[Any]:
    import capo_bedrock_agentcore_control.types.fallback_target

    return [
        capo_bedrock_agentcore_control.types.fallback_target.redact_sensitive(item)
        for item in value
    ]
