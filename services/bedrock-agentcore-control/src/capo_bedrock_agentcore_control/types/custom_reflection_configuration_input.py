"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomReflectionConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input


class _CustomReflectionConfigurationInput_episodicReflectionOverride(
    TypedDict, closed=True
):
    episodicReflectionOverride: "capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.EpisodicOverrideReflectionConfigurationInput"


CustomReflectionConfigurationInput: TypeAlias = (
    _CustomReflectionConfigurationInput_episodicReflectionOverride | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomReflectionConfigurationInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomReflectionConfigurationInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "episodicReflectionOverride" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CustomReflectionConfigurationInput: no recognized variant key"
        )


def redact_sensitive(
    value: CustomReflectionConfigurationInput,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "episodicReflectionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        out["episodicReflectionOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.redact_sensitive(
                value["episodicReflectionOverride"]
            )
        )
    return out
