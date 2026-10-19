"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomExtractionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_extraction_override
    import capo_bedrock_agentcore_control.types.semantic_extraction_override
    import capo_bedrock_agentcore_control.types.user_preference_extraction_override


class _CustomExtractionConfiguration_semanticExtractionOverride(TypedDict, closed=True):
    semanticExtractionOverride: "capo_bedrock_agentcore_control.types.semantic_extraction_override.SemanticExtractionOverride"


class _CustomExtractionConfiguration_userPreferenceExtractionOverride(
    TypedDict, closed=True
):
    userPreferenceExtractionOverride: "capo_bedrock_agentcore_control.types.user_preference_extraction_override.UserPreferenceExtractionOverride"


class _CustomExtractionConfiguration_episodicExtractionOverride(TypedDict, closed=True):
    episodicExtractionOverride: "capo_bedrock_agentcore_control.types.episodic_extraction_override.EpisodicExtractionOverride"


CustomExtractionConfiguration: TypeAlias = (
    _CustomExtractionConfiguration_semanticExtractionOverride
    | _CustomExtractionConfiguration_userPreferenceExtractionOverride
    | _CustomExtractionConfiguration_episodicExtractionOverride
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomExtractionConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomExtractionConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "semanticExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_extraction_override

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_extraction_override.serialize_json(
                value["semanticExtractionOverride"]
            )
        }
    elif "userPreferenceExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_extraction_override

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_extraction_override.serialize_json(
                value["userPreferenceExtractionOverride"]
            )
        }
    elif "episodicExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_extraction_override

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_extraction_override.serialize_json(
                value["episodicExtractionOverride"]
            )
        }
    else:
        raise SerializationError("CustomExtractionConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomExtractionConfiguration:
    if data.get("semanticExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.semantic_extraction_override

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_extraction_override.deserialize_json(
                data["semanticExtractionOverride"]
            )
        }
    elif data.get("userPreferenceExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_extraction_override

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_extraction_override.deserialize_json(
                data["userPreferenceExtractionOverride"]
            )
        }
    elif data.get("episodicExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_extraction_override

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_extraction_override.deserialize_json(
                data["episodicExtractionOverride"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CustomExtractionConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: CustomExtractionConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "semanticExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_extraction_override

        out["semanticExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.semantic_extraction_override.redact_sensitive(
                value["semanticExtractionOverride"]
            )
        )
    if "userPreferenceExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_extraction_override

        out["userPreferenceExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.user_preference_extraction_override.redact_sensitive(
                value["userPreferenceExtractionOverride"]
            )
        )
    if "episodicExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_extraction_override

        out["episodicExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_extraction_override.redact_sensitive(
                value["episodicExtractionOverride"]
            )
        )
    return out
