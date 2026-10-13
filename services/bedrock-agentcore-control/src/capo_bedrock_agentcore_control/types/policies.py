"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Policies``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.policy

Policies: TypeAlias = list["capo_bedrock_agentcore_control.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: Policies) -> list:
    import capo_bedrock_agentcore_control.types.policy

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore_control.types.policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Policies:
    import capo_bedrock_agentcore_control.types.policy

    out: Policies = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore_control.types.policy.deserialize_json(item))
    return out


def redact_sensitive(value: Policies) -> list[Any]:
    import capo_bedrock_agentcore_control.types.policy

    return [
        capo_bedrock_agentcore_control.types.policy.redact_sensitive(item)
        for item in value
    ]
