"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomExtractionConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input
    import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input


class _CustomExtractionConfigurationInput_semanticExtractionOverride(
    TypedDict, closed=True
):
    semanticExtractionOverride: "capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.SemanticOverrideExtractionConfigurationInput"


class _CustomExtractionConfigurationInput_userPreferenceExtractionOverride(
    TypedDict, closed=True
):
    userPreferenceExtractionOverride: "capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.UserPreferenceOverrideExtractionConfigurationInput"


class _CustomExtractionConfigurationInput_episodicExtractionOverride(
    TypedDict, closed=True
):
    episodicExtractionOverride: "capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.EpisodicOverrideExtractionConfigurationInput"


CustomExtractionConfigurationInput: TypeAlias = (
    _CustomExtractionConfigurationInput_semanticExtractionOverride
    | _CustomExtractionConfigurationInput_userPreferenceExtractionOverride
    | _CustomExtractionConfigurationInput_episodicExtractionOverride
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomExtractionConfigurationInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomExtractionConfigurationInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "semanticExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.serialize_json(
                value["semanticExtractionOverride"]
            )
        }
    elif "userPreferenceExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.serialize_json(
                value["userPreferenceExtractionOverride"]
            )
        }
    elif "episodicExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.serialize_json(
                value["episodicExtractionOverride"]
            )
        }
    else:
        raise SerializationError(
            "CustomExtractionConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> CustomExtractionConfigurationInput:
    if data.get("semanticExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        return {
            "semanticExtractionOverride": capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.deserialize_json(
                data["semanticExtractionOverride"]
            )
        }
    elif data.get("userPreferenceExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        return {
            "userPreferenceExtractionOverride": capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.deserialize_json(
                data["userPreferenceExtractionOverride"]
            )
        }
    elif data.get("episodicExtractionOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        return {
            "episodicExtractionOverride": capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.deserialize_json(
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
            "CustomExtractionConfigurationInput: no recognized variant key"
        )


def redact_sensitive(value: CustomExtractionConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "semanticExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["semanticExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.redact_sensitive(
                value["semanticExtractionOverride"]
            )
        )
    if "userPreferenceExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input

        out["userPreferenceExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.user_preference_override_extraction_configuration_input.redact_sensitive(
                value["userPreferenceExtractionOverride"]
            )
        )
    if "episodicExtractionOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        out["episodicExtractionOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.redact_sensitive(
                value["episodicExtractionOverride"]
            )
        )
    return out
