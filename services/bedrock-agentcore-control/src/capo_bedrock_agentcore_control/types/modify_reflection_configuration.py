"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyReflectionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_reflection_configuration_input
    import capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input


class ModifyReflectionConfigurationEpisodicReflectionConfigurationMember(
    TypedDict, closed=True
):
    episodicReflectionConfiguration: "capo_bedrock_agentcore_control.types.episodic_reflection_configuration_input.EpisodicReflectionConfigurationInput"


class ModifyReflectionConfigurationCustomReflectionConfigurationMember(
    TypedDict, closed=True
):
    customReflectionConfiguration: "capo_bedrock_agentcore_control.types.custom_reflection_configuration_input.CustomReflectionConfigurationInput"


ModifyReflectionConfiguration: TypeAlias = (
    ModifyReflectionConfigurationEpisodicReflectionConfigurationMember
    | ModifyReflectionConfigurationCustomReflectionConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyReflectionConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModifyReflectionConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "episodicReflectionConfiguration" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
