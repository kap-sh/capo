"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_configuration

ResourceConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.resource_configuration.ResourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.resource_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.resource_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceConfigurations:
    import capo_bedrock_agentcore_control.types.resource_configuration

    out: ResourceConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.resource_configuration.deserialize_json(
                item
            )
        )
    return out
