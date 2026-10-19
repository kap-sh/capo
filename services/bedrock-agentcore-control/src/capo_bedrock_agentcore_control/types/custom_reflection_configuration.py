"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomReflectionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_reflection_override


class _CustomReflectionConfiguration_episodicReflectionOverride(TypedDict, closed=True):
    episodicReflectionOverride: "capo_bedrock_agentcore_control.types.episodic_reflection_override.EpisodicReflectionOverride"


CustomReflectionConfiguration: TypeAlias = (
    _CustomReflectionConfiguration_episodicReflectionOverride | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomReflectionConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomReflectionConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "episodicReflectionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_override

        return {
            "episodicReflectionOverride": capo_bedrock_agentcore_control.types.episodic_reflection_override.serialize_json(
                value["episodicReflectionOverride"]
            )
        }
    else:
        raise SerializationError("CustomReflectionConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomReflectionConfiguration:
    if data.get("episodicReflectionOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_reflection_override

        return {
            "episodicReflectionOverride": capo_bedrock_agentcore_control.types.episodic_reflection_override.deserialize_json(
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
            "CustomReflectionConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: CustomReflectionConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "episodicReflectionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_reflection_override

        out["episodicReflectionOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_reflection_override.redact_sensitive(
                value["episodicReflectionOverride"]
            )
        )
    return out
