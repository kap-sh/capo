"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_configuration_input
    import capo_bedrock_agentcore_control.types.self_managed_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_configuration_input
    import capo_bedrock_agentcore_control.types.summary_override_configuration_input
    import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input


class _CustomConfigurationInput_semanticOverride(TypedDict, closed=True):
    semanticOverride: "capo_bedrock_agentcore_control.types.semantic_override_configuration_input.SemanticOverrideConfigurationInput"


class _CustomConfigurationInput_summaryOverride(TypedDict, closed=True):
    summaryOverride: "capo_bedrock_agentcore_control.types.summary_override_configuration_input.SummaryOverrideConfigurationInput"


class _CustomConfigurationInput_userPreferenceOverride(TypedDict, closed=True):
    userPreferenceOverride: "capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.UserPreferenceOverrideConfigurationInput"


class _CustomConfigurationInput_episodicOverride(TypedDict, closed=True):
    episodicOverride: "capo_bedrock_agentcore_control.types.episodic_override_configuration_input.EpisodicOverrideConfigurationInput"


class _CustomConfigurationInput_selfManagedConfiguration(TypedDict, closed=True):
    selfManagedConfiguration: "capo_bedrock_agentcore_control.types.self_managed_configuration_input.SelfManagedConfigurationInput"


CustomConfigurationInput: TypeAlias = (
    _CustomConfigurationInput_semanticOverride
    | _CustomConfigurationInput_summaryOverride
    | _CustomConfigurationInput_userPreferenceOverride
    | _CustomConfigurationInput_episodicOverride
    | _CustomConfigurationInput_selfManagedConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConfigurationInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomConfigurationInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "semanticOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_configuration_input

        return {
            "semanticOverride": capo_bedrock_agentcore_control.types.semantic_override_configuration_input.serialize_json(
                value["semanticOverride"]
            )
        }
    elif "summaryOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_override_configuration_input

        return {
            "summaryOverride": capo_bedrock_agentcore_control.types.summary_override_configuration_input.serialize_json(
                value["summaryOverride"]
            )
        }
    elif "userPreferenceOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input

        return {
            "userPreferenceOverride": capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.serialize_json(
                value["userPreferenceOverride"]
            )
        }
    elif "episodicOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_configuration_input

        return {
            "episodicOverride": capo_bedrock_agentcore_control.types.episodic_override_configuration_input.serialize_json(
                value["episodicOverride"]
            )
        }
    elif "selfManagedConfiguration" in value:
        import capo_bedrock_agentcore_control.types.self_managed_configuration_input

        return {
            "selfManagedConfiguration": capo_bedrock_agentcore_control.types.self_managed_configuration_input.serialize_json(
                value["selfManagedConfiguration"]
            )
        }
    else:
        raise SerializationError("CustomConfigurationInput: no variant present")


def deserialize_json(data: dict) -> CustomConfigurationInput:
    if data.get("semanticOverride") is not None:
        import capo_bedrock_agentcore_control.types.semantic_override_configuration_input

        return {
            "semanticOverride": capo_bedrock_agentcore_control.types.semantic_override_configuration_input.deserialize_json(
                data["semanticOverride"]
            )
        }
    elif data.get("summaryOverride") is not None:
        import capo_bedrock_agentcore_control.types.summary_override_configuration_input

        return {
            "summaryOverride": capo_bedrock_agentcore_control.types.summary_override_configuration_input.deserialize_json(
                data["summaryOverride"]
            )
        }
    elif data.get("userPreferenceOverride") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input

        return {
            "userPreferenceOverride": capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.deserialize_json(
                data["userPreferenceOverride"]
            )
        }
    elif data.get("episodicOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_configuration_input

        return {
            "episodicOverride": capo_bedrock_agentcore_control.types.episodic_override_configuration_input.deserialize_json(
                data["episodicOverride"]
            )
        }
    elif data.get("selfManagedConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.self_managed_configuration_input

        return {
            "selfManagedConfiguration": capo_bedrock_agentcore_control.types.self_managed_configuration_input.deserialize_json(
                data["selfManagedConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CustomConfigurationInput: no recognized variant key"
        )


def redact_sensitive(
    value: CustomConfigurationInput,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "semanticOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_configuration_input

        out["semanticOverride"] = (
            capo_bedrock_agentcore_control.types.semantic_override_configuration_input.redact_sensitive(
                value["semanticOverride"]
            )
        )
    if "summaryOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_override_configuration_input

        out["summaryOverride"] = (
            capo_bedrock_agentcore_control.types.summary_override_configuration_input.redact_sensitive(
                value["summaryOverride"]
            )
        )
    if "userPreferenceOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_configuration_input

        out["userPreferenceOverride"] = (
            capo_bedrock_agentcore_control.types.user_preference_override_configuration_input.redact_sensitive(
                value["userPreferenceOverride"]
            )
        )
    if "episodicOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_configuration_input

        out["episodicOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_override_configuration_input.redact_sensitive(
                value["episodicOverride"]
            )
        )
    return out
