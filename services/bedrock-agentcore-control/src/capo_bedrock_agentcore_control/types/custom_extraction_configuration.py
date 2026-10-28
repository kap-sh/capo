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


class CustomExtractionConfigurationSemanticExtractionOverrideMember(
    TypedDict, closed=True
):
    semanticExtractionOverride: "capo_bedrock_agentcore_control.types.semantic_extraction_override.SemanticExtractionOverride"


class CustomExtractionConfigurationUserPreferenceExtractionOverrideMember(
    TypedDict, closed=True
):
    userPreferenceExtractionOverride: "capo_bedrock_agentcore_control.types.user_preference_extraction_override.UserPreferenceExtractionOverride"


class CustomExtractionConfigurationEpisodicExtractionOverrideMember(
    TypedDict, closed=True
):
    episodicExtractionOverride: "capo_bedrock_agentcore_control.types.episodic_extraction_override.EpisodicExtractionOverride"


CustomExtractionConfiguration: TypeAlias = (
    CustomExtractionConfigurationSemanticExtractionOverrideMember
    | CustomExtractionConfigurationUserPreferenceExtractionOverrideMember
    | CustomExtractionConfigurationEpisodicExtractionOverrideMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomExtractionConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomExtractionConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CustomExtractionConfiguration: no recognized variant key"
        )


def redact_sensitive(value: CustomExtractionConfiguration) -> dict[str, Any]:
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
