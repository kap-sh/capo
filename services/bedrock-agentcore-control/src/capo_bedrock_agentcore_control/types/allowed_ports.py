"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedPorts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_port

AllowedPorts: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.allowed_port.AllowedPort"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedPorts) -> list:
    import capo_bedrock_agentcore_control.types.allowed_port

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.allowed_port.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AllowedPorts:
    import capo_bedrock_agentcore_control.types.allowed_port

    out: AllowedPorts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.allowed_port.deserialize_json(item)
        )
    return out
