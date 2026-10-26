"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
    import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input
    import capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input


class _CustomConsolidationConfigurationInput_semanticConsolidationOverride(
    TypedDict, closed=True
):
    semanticConsolidationOverride: "capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.SemanticOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_summaryConsolidationOverride(
    TypedDict, closed=True
):
    summaryConsolidationOverride: "capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.SummaryOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_userPreferenceConsolidationOverride(
    TypedDict, closed=True
):
    userPreferenceConsolidationOverride: "capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.UserPreferenceOverrideConsolidationConfigurationInput"


class _CustomConsolidationConfigurationInput_episodicConsolidationOverride(
    TypedDict, closed=True
):
    episodicConsolidationOverride: "capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.EpisodicOverrideConsolidationConfigurationInput"


CustomConsolidationConfigurationInput: TypeAlias = (
    _CustomConsolidationConfigurationInput_semanticConsolidationOverride
    | _CustomConsolidationConfigurationInput_summaryConsolidationOverride
    | _CustomConsolidationConfigurationInput_userPreferenceConsolidationOverride
    | _CustomConsolidationConfigurationInput_episodicConsolidationOverride
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConsolidationConfigurationInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomConsolidationConfigurationInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "semanticConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.serialize_json(
                value["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.serialize_json(
                value["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.serialize_json(
                value["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.serialize_json(
                value["episodicConsolidationOverride"]
            )
        }
    else:
        raise SerializationError(
            "CustomConsolidationConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> CustomConsolidationConfigurationInput:
    if data.get("semanticConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.deserialize_json(
                data["semanticConsolidationOverride"]
            )
        }
    elif data.get("summaryConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.deserialize_json(
                data["summaryConsolidationOverride"]
            )
        }
    elif data.get("userPreferenceConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.deserialize_json(
                data["userPreferenceConsolidationOverride"]
            )
        }
    elif data.get("episodicConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.deserialize_json(
                data["episodicConsolidationOverride"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CustomConsolidationConfigurationInput: no recognized variant key"
        )


def redact_sensitive(value: CustomConsolidationConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "semanticConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["semanticConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.redact_sensitive(
                value["semanticConsolidationOverride"]
            )
        )
    if "summaryConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        out["summaryConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.redact_sensitive(
                value["summaryConsolidationOverride"]
            )
        )
    if "userPreferenceConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input

        out["userPreferenceConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.user_preference_override_consolidation_configuration_input.redact_sensitive(
                value["userPreferenceConsolidationOverride"]
            )
        )
    if "episodicConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        out["episodicConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.redact_sensitive(
                value["episodicConsolidationOverride"]
            )
        )
    return out
