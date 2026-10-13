"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Actions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.action

Actions: TypeAlias = list["capo_bedrock_agentcore_control.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: Actions) -> list:
    import capo_bedrock_agentcore_control.types.action

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore_control.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> Actions:
    import capo_bedrock_agentcore_control.types.action

    out: Actions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore_control.types.action.deserialize_json(item))
    return out


def redact_sensitive(value: Actions) -> list[Any]:
    import capo_bedrock_agentcore_control.types.action

    return [
        capo_bedrock_agentcore_control.types.action.redact_sensitive(item)
        for item in value
    ]
