"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComponentConfigurationMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.component_configuration
    import capo_bedrock_agentcore_control.types.component_identifier

ComponentConfigurationMap: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.component_identifier.ComponentIdentifier",
    "capo_bedrock_agentcore_control.types.component_configuration.ComponentConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_agentcore_control.types.component_configuration

        out[key] = (
            capo_bedrock_agentcore_control.types.component_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentConfigurationMap:
    out: ComponentConfigurationMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_agentcore_control.types.component_configuration

        out[key] = (
            capo_bedrock_agentcore_control.types.component_configuration.deserialize_json(
                value
            )
        )
    return out


def redact_sensitive(value: ComponentConfigurationMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
