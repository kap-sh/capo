"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ReflectionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_reflection_configuration
    import capo_bedrock_agentcore_control.types.episodic_reflection_configuration


class _ReflectionConfiguration_customReflectionConfiguration(TypedDict, closed=True):
    customReflectionConfiguration: "capo_bedrock_agentcore_control.types.custom_reflection_configuration.CustomReflectionConfiguration"


class _ReflectionConfiguration_episodicReflectionConfiguration(TypedDict, closed=True):
    episodicReflectionConfiguration: "capo_bedrock_agentcore_control.types.episodic_reflection_configuration.EpisodicReflectionConfiguration"


ReflectionConfiguration: TypeAlias = (
    _ReflectionConfiguration_customReflectionConfiguration
    | _ReflectionConfiguration_episodicReflectionConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReflectionConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReflectionConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration

        return {
            "customReflectionConfiguration": capo_bedrock_agentcore_control.types.custom_reflection_configuration.serialize_json(
                value["customReflectionConfiguration"]
            )
        }
    elif "episodicReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration

        return {
            "episodicReflectionConfiguration": capo_bedrock_agentcore_control.types.episodic_reflection_configuration.serialize_json(
                value["episodicReflectionConfiguration"]
            )
        }
    else:
        raise SerializationError("ReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> ReflectionConfiguration:
    if data.get("customReflectionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration

        return {
            "customReflectionConfiguration": capo_bedrock_agentcore_control.types.custom_reflection_configuration.deserialize_json(
                data["customReflectionConfiguration"]
            )
        }
    elif data.get("episodicReflectionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration

        return {
            "episodicReflectionConfiguration": capo_bedrock_agentcore_control.types.episodic_reflection_configuration.deserialize_json(
                data["episodicReflectionConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ReflectionConfiguration: no recognized variant key")


def redact_sensitive(value: ReflectionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_reflection_configuration

        out["customReflectionConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_reflection_configuration.redact_sensitive(
                value["customReflectionConfiguration"]
            )
        )
    if "episodicReflectionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_configuration

        out["episodicReflectionConfiguration"] = (
            capo_bedrock_agentcore_control.types.episodic_reflection_configuration.redact_sensitive(
                value["episodicReflectionConfiguration"]
            )
        )
    return out
