"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomReflectionConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input


class _CustomReflectionConfigurationInput_episodicReflectionOverride(
    TypedDict, closed=True
):
    episodicReflectionOverride: "capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.EpisodicOverrideReflectionConfigurationInput"


CustomReflectionConfigurationInput: TypeAlias = (
    _CustomReflectionConfigurationInput_episodicReflectionOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomReflectionConfigurationInput) -> dict:
    if "episodicReflectionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        return {
            "episodicReflectionOverride": capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.serialize_json(
                value["episodicReflectionOverride"]
            )
        }
    else:
        raise SerializationError(
            "CustomReflectionConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> CustomReflectionConfigurationInput:
    if data.get("episodicReflectionOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        return {
            "episodicReflectionOverride": capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.deserialize_json(
                data["episodicReflectionOverride"]
            )
        }
    else:
        raise DeserializationError(
            "CustomReflectionConfigurationInput: no recognized variant key"
        )


def redact_sensitive(value: CustomReflectionConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "episodicReflectionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        out["episodicReflectionOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.redact_sensitive(
                value["episodicReflectionOverride"]
            )
        )
    return out
