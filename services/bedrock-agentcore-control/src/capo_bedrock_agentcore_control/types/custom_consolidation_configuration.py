"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomConsolidationConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_consolidation_override
    import capo_bedrock_agentcore_control.types.semantic_consolidation_override
    import capo_bedrock_agentcore_control.types.summary_consolidation_override
    import capo_bedrock_agentcore_control.types.user_preference_consolidation_override


class CustomConsolidationConfigurationSemanticConsolidationOverrideMember(
    TypedDict, closed=True
):
    semanticConsolidationOverride: "capo_bedrock_agentcore_control.types.semantic_consolidation_override.SemanticConsolidationOverride"


class CustomConsolidationConfigurationSummaryConsolidationOverrideMember(
    TypedDict, closed=True
):
    summaryConsolidationOverride: "capo_bedrock_agentcore_control.types.summary_consolidation_override.SummaryConsolidationOverride"


class CustomConsolidationConfigurationUserPreferenceConsolidationOverrideMember(
    TypedDict, closed=True
):
    userPreferenceConsolidationOverride: "capo_bedrock_agentcore_control.types.user_preference_consolidation_override.UserPreferenceConsolidationOverride"


class CustomConsolidationConfigurationEpisodicConsolidationOverrideMember(
    TypedDict, closed=True
):
    episodicConsolidationOverride: "capo_bedrock_agentcore_control.types.episodic_consolidation_override.EpisodicConsolidationOverride"


CustomConsolidationConfiguration: TypeAlias = (
    CustomConsolidationConfigurationSemanticConsolidationOverrideMember
    | CustomConsolidationConfigurationSummaryConsolidationOverrideMember
    | CustomConsolidationConfigurationUserPreferenceConsolidationOverrideMember
    | CustomConsolidationConfigurationEpisodicConsolidationOverrideMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomConsolidationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomConsolidationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "semanticConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_consolidation_override.serialize_json(
                value["semanticConsolidationOverride"]
            )
        }
    elif "summaryConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_consolidation_override.serialize_json(
                value["summaryConsolidationOverride"]
            )
        }
    elif "userPreferenceConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_consolidation_override.serialize_json(
                value["userPreferenceConsolidationOverride"]
            )
        }
    elif "episodicConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_consolidation_override.serialize_json(
                value["episodicConsolidationOverride"]
            )
        }
    else:
        raise SerializationError("CustomConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> CustomConsolidationConfiguration:
    if data.get("semanticConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.semantic_consolidation_override

        return {
            "semanticConsolidationOverride": capo_bedrock_agentcore_control.types.semantic_consolidation_override.deserialize_json(
                data["semanticConsolidationOverride"]
            )
        }
    elif data.get("summaryConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.summary_consolidation_override

        return {
            "summaryConsolidationOverride": capo_bedrock_agentcore_control.types.summary_consolidation_override.deserialize_json(
                data["summaryConsolidationOverride"]
            )
        }
    elif data.get("userPreferenceConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.user_preference_consolidation_override

        return {
            "userPreferenceConsolidationOverride": capo_bedrock_agentcore_control.types.user_preference_consolidation_override.deserialize_json(
                data["userPreferenceConsolidationOverride"]
            )
        }
    elif data.get("episodicConsolidationOverride") is not None:
        import capo_bedrock_agentcore_control.types.episodic_consolidation_override

        return {
            "episodicConsolidationOverride": capo_bedrock_agentcore_control.types.episodic_consolidation_override.deserialize_json(
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
            "CustomConsolidationConfiguration: no recognized variant key"
        )


def redact_sensitive(value: CustomConsolidationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "semanticConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.semantic_consolidation_override

        out["semanticConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.semantic_consolidation_override.redact_sensitive(
                value["semanticConsolidationOverride"]
            )
        )
    if "summaryConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.summary_consolidation_override

        out["summaryConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.summary_consolidation_override.redact_sensitive(
                value["summaryConsolidationOverride"]
            )
        )
    if "userPreferenceConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.user_preference_consolidation_override

        out["userPreferenceConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.user_preference_consolidation_override.redact_sensitive(
                value["userPreferenceConsolidationOverride"]
            )
        )
    if "episodicConsolidationOverride" in value:
        import capo_bedrock_agentcore_control.types.episodic_consolidation_override

        out["episodicConsolidationOverride"] = (
            capo_bedrock_agentcore_control.types.episodic_consolidation_override.redact_sensitive(
                value["episodicConsolidationOverride"]
            )
        )
    return out
