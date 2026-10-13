"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyReflectionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_reflection_configuration_input
    import capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input


class _ModifyReflectionConfiguration_episodicReflectionConfiguration(
    TypedDict, closed=True
):
    episodicReflectionConfiguration: "capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input.EpisodicReflectionConfigurationInput"


class _ModifyReflectionConfiguration_customReflectionConfiguration(
    TypedDict, closed=True
):
    customReflectionConfiguration: "capo_bedrock_agentcore_control.types.custom_reflection_configuration_input.CustomReflectionConfigurationInput"


ModifyReflectionConfiguration: TypeAlias = (
    _ModifyReflectionConfiguration_episodicReflectionConfiguration
    | _ModifyReflectionConfiguration_customReflectionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyReflectionConfiguration) -> dict:
    if "episodicReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input

        return {
            "episodicReflectionConfiguration": capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input.serialize_json(
                value["episodicReflectionConfiguration"]
            )
        }
    elif "customReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration_input

        return {
            "customReflectionConfiguration": capo_bedrock_agentcore_control.types.custom_reflection_configuration_input.serialize_json(
                value["customReflectionConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyReflectionConfiguration:
    if data.get("episodicReflectionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input

        return {
            "episodicReflectionConfiguration": capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input.deserialize_json(
                data["episodicReflectionConfiguration"]
            )
        }
    elif data.get("customReflectionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration_input

        return {
            "customReflectionConfiguration": capo_bedrock_agentcore_control.types.custom_reflection_configuration_input.deserialize_json(
                data["customReflectionConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ModifyReflectionConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ModifyReflectionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "episodicReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input

        out["episodicReflectionConfiguration"] = (
            capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input.redact_sensitive(
                value["episodicReflectionConfiguration"]
            )
        )
    if "customReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration_input

        out["customReflectionConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_reflection_configuration_input.redact_sensitive(
                value["customReflectionConfiguration"]
            )
        )
    return out
