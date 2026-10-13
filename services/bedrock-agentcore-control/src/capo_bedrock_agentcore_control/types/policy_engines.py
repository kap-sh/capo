"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngines``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.policy_engine

PolicyEngines: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.policy_engine.PolicyEngine"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEngines) -> list:
    import capo_bedrock_agentcore_control.types.policy_engine

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.policy_engine.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PolicyEngines:
    import capo_bedrock_agentcore_control.types.policy_engine

    out: PolicyEngines = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.policy_engine.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PolicyEngines) -> list[Any]:
    import capo_bedrock_agentcore_control.types.policy_engine

    return [
        capo_bedrock_agentcore_control.types.policy_engine.redact_sensitive(item)
        for item in value
    ]
