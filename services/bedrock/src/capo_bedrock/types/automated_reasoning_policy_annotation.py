"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_add_rule_annotation
    import capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation
    import capo_bedrock.types.automated_reasoning_policy_add_type_annotation
    import capo_bedrock.types.automated_reasoning_policy_add_variable_annotation
    import capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation
    import capo_bedrock.types.automated_reasoning_policy_delete_type_annotation
    import capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation
    import capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation
    import capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation
    import capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation
    import capo_bedrock.types.automated_reasoning_policy_update_rule_annotation
    import capo_bedrock.types.automated_reasoning_policy_update_type_annotation
    import capo_bedrock.types.automated_reasoning_policy_update_variable_annotation


class _AutomatedReasoningPolicyAnnotation_addType(TypedDict, closed=True):
    addType: "capo_bedrock.types.automated_reasoning_policy_add_type_annotation.AutomatedReasoningPolicyAddTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateType(TypedDict, closed=True):
    updateType: "capo_bedrock.types.automated_reasoning_policy_update_type_annotation.AutomatedReasoningPolicyUpdateTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteType(TypedDict, closed=True):
    deleteType: "capo_bedrock.types.automated_reasoning_policy_delete_type_annotation.AutomatedReasoningPolicyDeleteTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_addVariable(TypedDict, closed=True):
    addVariable: "capo_bedrock.types.automated_reasoning_policy_add_variable_annotation.AutomatedReasoningPolicyAddVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateVariable(TypedDict, closed=True):
    updateVariable: "capo_bedrock.types.automated_reasoning_policy_update_variable_annotation.AutomatedReasoningPolicyUpdateVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteVariable(TypedDict, closed=True):
    deleteVariable: "capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation.AutomatedReasoningPolicyDeleteVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_addRule(TypedDict, closed=True):
    addRule: "capo_bedrock.types.automated_reasoning_policy_add_rule_annotation.AutomatedReasoningPolicyAddRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateRule(TypedDict, closed=True):
    updateRule: "capo_bedrock.types.automated_reasoning_policy_update_rule_annotation.AutomatedReasoningPolicyUpdateRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteRule(TypedDict, closed=True):
    deleteRule: "capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation.AutomatedReasoningPolicyDeleteRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_addRuleFromNaturalLanguage(
    TypedDict, closed=True
):
    addRuleFromNaturalLanguage: "capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateFromRulesFeedback(
    TypedDict, closed=True
):
    updateFromRulesFeedback: "capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateFromScenarioFeedback(
    TypedDict, closed=True
):
    updateFromScenarioFeedback: "capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation"


class _AutomatedReasoningPolicyAnnotation_ingestContent(TypedDict, closed=True):
    ingestContent: "capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation.AutomatedReasoningPolicyIngestContentAnnotation"


AutomatedReasoningPolicyAnnotation: TypeAlias = (
    _AutomatedReasoningPolicyAnnotation_addType
    | _AutomatedReasoningPolicyAnnotation_updateType
    | _AutomatedReasoningPolicyAnnotation_deleteType
    | _AutomatedReasoningPolicyAnnotation_addVariable
    | _AutomatedReasoningPolicyAnnotation_updateVariable
    | _AutomatedReasoningPolicyAnnotation_deleteVariable
    | _AutomatedReasoningPolicyAnnotation_addRule
    | _AutomatedReasoningPolicyAnnotation_updateRule
    | _AutomatedReasoningPolicyAnnotation_deleteRule
    | _AutomatedReasoningPolicyAnnotation_addRuleFromNaturalLanguage
    | _AutomatedReasoningPolicyAnnotation_updateFromRulesFeedback
    | _AutomatedReasoningPolicyAnnotation_updateFromScenarioFeedback
    | _AutomatedReasoningPolicyAnnotation_ingestContent
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotation) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AutomatedReasoningPolicyAnnotation: cannot serialize unknown variant {value.name!r}"
        )
    elif "addType" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_annotation

        return {
            "addType": capo_bedrock.types.automated_reasoning_policy_add_type_annotation.serialize_json(
                value["addType"]
            )
        }
    elif "updateType" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_annotation

        return {
            "updateType": capo_bedrock.types.automated_reasoning_policy_update_type_annotation.serialize_json(
                value["updateType"]
            )
        }
    elif "deleteType" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_annotation

        return {
            "deleteType": capo_bedrock.types.automated_reasoning_policy_delete_type_annotation.serialize_json(
                value["deleteType"]
            )
        }
    elif "addVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_annotation

        return {
            "addVariable": capo_bedrock.types.automated_reasoning_policy_add_variable_annotation.serialize_json(
                value["addVariable"]
            )
        }
    elif "updateVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_annotation

        return {
            "updateVariable": capo_bedrock.types.automated_reasoning_policy_update_variable_annotation.serialize_json(
                value["updateVariable"]
            )
        }
    elif "deleteVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation

        return {
            "deleteVariable": capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation.serialize_json(
                value["deleteVariable"]
            )
        }
    elif "addRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_annotation

        return {
            "addRule": capo_bedrock.types.automated_reasoning_policy_add_rule_annotation.serialize_json(
                value["addRule"]
            )
        }
    elif "updateRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_annotation

        return {
            "updateRule": capo_bedrock.types.automated_reasoning_policy_update_rule_annotation.serialize_json(
                value["updateRule"]
            )
        }
    elif "deleteRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation

        return {
            "deleteRule": capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation.serialize_json(
                value["deleteRule"]
            )
        }
    elif "addRuleFromNaturalLanguage" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation

        return {
            "addRuleFromNaturalLanguage": capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.serialize_json(
                value["addRuleFromNaturalLanguage"]
            )
        }
    elif "updateFromRulesFeedback" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation

        return {
            "updateFromRulesFeedback": capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.serialize_json(
                value["updateFromRulesFeedback"]
            )
        }
    elif "updateFromScenarioFeedback" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation

        return {
            "updateFromScenarioFeedback": capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.serialize_json(
                value["updateFromScenarioFeedback"]
            )
        }
    elif "ingestContent" in value:
        import capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation

        return {
            "ingestContent": capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation.serialize_json(
                value["ingestContent"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyAnnotation: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotation:
    if data.get("addType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_type_annotation

        return {
            "addType": capo_bedrock.types.automated_reasoning_policy_add_type_annotation.deserialize_json(
                data["addType"]
            )
        }
    elif data.get("updateType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_type_annotation

        return {
            "updateType": capo_bedrock.types.automated_reasoning_policy_update_type_annotation.deserialize_json(
                data["updateType"]
            )
        }
    elif data.get("deleteType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_annotation

        return {
            "deleteType": capo_bedrock.types.automated_reasoning_policy_delete_type_annotation.deserialize_json(
                data["deleteType"]
            )
        }
    elif data.get("addVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_annotation

        return {
            "addVariable": capo_bedrock.types.automated_reasoning_policy_add_variable_annotation.deserialize_json(
                data["addVariable"]
            )
        }
    elif data.get("updateVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_annotation

        return {
            "updateVariable": capo_bedrock.types.automated_reasoning_policy_update_variable_annotation.deserialize_json(
                data["updateVariable"]
            )
        }
    elif data.get("deleteVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation

        return {
            "deleteVariable": capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation.deserialize_json(
                data["deleteVariable"]
            )
        }
    elif data.get("addRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_annotation

        return {
            "addRule": capo_bedrock.types.automated_reasoning_policy_add_rule_annotation.deserialize_json(
                data["addRule"]
            )
        }
    elif data.get("updateRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_annotation

        return {
            "updateRule": capo_bedrock.types.automated_reasoning_policy_update_rule_annotation.deserialize_json(
                data["updateRule"]
            )
        }
    elif data.get("deleteRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation

        return {
            "deleteRule": capo_bedrock.types.automated_reasoning_policy_delete_rule_annotation.deserialize_json(
                data["deleteRule"]
            )
        }
    elif data.get("addRuleFromNaturalLanguage") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation

        return {
            "addRuleFromNaturalLanguage": capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.deserialize_json(
                data["addRuleFromNaturalLanguage"]
            )
        }
    elif data.get("updateFromRulesFeedback") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation

        return {
            "updateFromRulesFeedback": capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.deserialize_json(
                data["updateFromRulesFeedback"]
            )
        }
    elif data.get("updateFromScenarioFeedback") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation

        return {
            "updateFromScenarioFeedback": capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.deserialize_json(
                data["updateFromScenarioFeedback"]
            )
        }
    elif data.get("ingestContent") is not None:
        import capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation

        return {
            "ingestContent": capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation.deserialize_json(
                data["ingestContent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotation: no recognized variant key"
        )


def redact_sensitive(
    value: AutomatedReasoningPolicyAnnotation,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "addType" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_annotation

        out["addType"] = (
            capo_bedrock.types.automated_reasoning_policy_add_type_annotation.redact_sensitive(
                value["addType"]
            )
        )
    if "updateType" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_annotation

        out["updateType"] = (
            capo_bedrock.types.automated_reasoning_policy_update_type_annotation.redact_sensitive(
                value["updateType"]
            )
        )
    if "deleteType" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_annotation

        out["deleteType"] = (
            capo_bedrock.types.automated_reasoning_policy_delete_type_annotation.redact_sensitive(
                value["deleteType"]
            )
        )
    if "addVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_annotation

        out["addVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_add_variable_annotation.redact_sensitive(
                value["addVariable"]
            )
        )
    if "updateVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_annotation

        out["updateVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_update_variable_annotation.redact_sensitive(
                value["updateVariable"]
            )
        )
    if "deleteVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation

        out["deleteVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_delete_variable_annotation.redact_sensitive(
                value["deleteVariable"]
            )
        )
    if "addRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_annotation

        out["addRule"] = (
            capo_bedrock.types.automated_reasoning_policy_add_rule_annotation.redact_sensitive(
                value["addRule"]
            )
        )
    if "updateRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_annotation

        out["updateRule"] = (
            capo_bedrock.types.automated_reasoning_policy_update_rule_annotation.redact_sensitive(
                value["updateRule"]
            )
        )
    if "addRuleFromNaturalLanguage" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation

        out["addRuleFromNaturalLanguage"] = (
            capo_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.redact_sensitive(
                value["addRuleFromNaturalLanguage"]
            )
        )
    if "updateFromRulesFeedback" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation

        out["updateFromRulesFeedback"] = (
            capo_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.redact_sensitive(
                value["updateFromRulesFeedback"]
            )
        )
    if "updateFromScenarioFeedback" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation

        out["updateFromScenarioFeedback"] = (
            capo_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.redact_sensitive(
                value["updateFromScenarioFeedback"]
            )
        )
    if "ingestContent" in value:
        import capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation

        out["ingestContent"] = (
            capo_bedrock.types.automated_reasoning_policy_ingest_content_annotation.redact_sensitive(
                value["ingestContent"]
            )
        )
    return out
