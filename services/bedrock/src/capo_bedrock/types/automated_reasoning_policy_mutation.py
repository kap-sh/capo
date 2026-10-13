"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyMutation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_add_rule_mutation
    import capo_bedrock.types.automated_reasoning_policy_add_type_mutation
    import capo_bedrock.types.automated_reasoning_policy_add_variable_mutation
    import capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation
    import capo_bedrock.types.automated_reasoning_policy_delete_type_mutation
    import capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation
    import capo_bedrock.types.automated_reasoning_policy_update_rule_mutation
    import capo_bedrock.types.automated_reasoning_policy_update_type_mutation
    import capo_bedrock.types.automated_reasoning_policy_update_variable_mutation


class _AutomatedReasoningPolicyMutation_addType(TypedDict, closed=True):
    addType: "capo_bedrock.types.automated_reasoning_policy_add_type_mutation.AutomatedReasoningPolicyAddTypeMutation"


class _AutomatedReasoningPolicyMutation_updateType(TypedDict, closed=True):
    updateType: "capo_bedrock.types.automated_reasoning_policy_update_type_mutation.AutomatedReasoningPolicyUpdateTypeMutation"


class _AutomatedReasoningPolicyMutation_deleteType(TypedDict, closed=True):
    deleteType: "capo_bedrock.types.automated_reasoning_policy_delete_type_mutation.AutomatedReasoningPolicyDeleteTypeMutation"


class _AutomatedReasoningPolicyMutation_addVariable(TypedDict, closed=True):
    addVariable: "capo_bedrock.types.automated_reasoning_policy_add_variable_mutation.AutomatedReasoningPolicyAddVariableMutation"


class _AutomatedReasoningPolicyMutation_updateVariable(TypedDict, closed=True):
    updateVariable: "capo_bedrock.types.automated_reasoning_policy_update_variable_mutation.AutomatedReasoningPolicyUpdateVariableMutation"


class _AutomatedReasoningPolicyMutation_deleteVariable(TypedDict, closed=True):
    deleteVariable: "capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation.AutomatedReasoningPolicyDeleteVariableMutation"


class _AutomatedReasoningPolicyMutation_addRule(TypedDict, closed=True):
    addRule: "capo_bedrock.types.automated_reasoning_policy_add_rule_mutation.AutomatedReasoningPolicyAddRuleMutation"


class _AutomatedReasoningPolicyMutation_updateRule(TypedDict, closed=True):
    updateRule: "capo_bedrock.types.automated_reasoning_policy_update_rule_mutation.AutomatedReasoningPolicyUpdateRuleMutation"


class _AutomatedReasoningPolicyMutation_deleteRule(TypedDict, closed=True):
    deleteRule: "capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation.AutomatedReasoningPolicyDeleteRuleMutation"


AutomatedReasoningPolicyMutation: TypeAlias = (
    _AutomatedReasoningPolicyMutation_addType
    | _AutomatedReasoningPolicyMutation_updateType
    | _AutomatedReasoningPolicyMutation_deleteType
    | _AutomatedReasoningPolicyMutation_addVariable
    | _AutomatedReasoningPolicyMutation_updateVariable
    | _AutomatedReasoningPolicyMutation_deleteVariable
    | _AutomatedReasoningPolicyMutation_addRule
    | _AutomatedReasoningPolicyMutation_updateRule
    | _AutomatedReasoningPolicyMutation_deleteRule
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyMutation) -> dict:
    if "addType" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_mutation

        return {
            "addType": capo_bedrock.types.automated_reasoning_policy_add_type_mutation.serialize_json(
                value["addType"]
            )
        }
    elif "updateType" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_mutation

        return {
            "updateType": capo_bedrock.types.automated_reasoning_policy_update_type_mutation.serialize_json(
                value["updateType"]
            )
        }
    elif "deleteType" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_mutation

        return {
            "deleteType": capo_bedrock.types.automated_reasoning_policy_delete_type_mutation.serialize_json(
                value["deleteType"]
            )
        }
    elif "addVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_mutation

        return {
            "addVariable": capo_bedrock.types.automated_reasoning_policy_add_variable_mutation.serialize_json(
                value["addVariable"]
            )
        }
    elif "updateVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_mutation

        return {
            "updateVariable": capo_bedrock.types.automated_reasoning_policy_update_variable_mutation.serialize_json(
                value["updateVariable"]
            )
        }
    elif "deleteVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation

        return {
            "deleteVariable": capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation.serialize_json(
                value["deleteVariable"]
            )
        }
    elif "addRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_mutation

        return {
            "addRule": capo_bedrock.types.automated_reasoning_policy_add_rule_mutation.serialize_json(
                value["addRule"]
            )
        }
    elif "updateRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_mutation

        return {
            "updateRule": capo_bedrock.types.automated_reasoning_policy_update_rule_mutation.serialize_json(
                value["updateRule"]
            )
        }
    elif "deleteRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation

        return {
            "deleteRule": capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation.serialize_json(
                value["deleteRule"]
            )
        }
    else:
        raise SerializationError("AutomatedReasoningPolicyMutation: no variant present")


def deserialize_json(data: dict) -> AutomatedReasoningPolicyMutation:
    if data.get("addType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_type_mutation

        return {
            "addType": capo_bedrock.types.automated_reasoning_policy_add_type_mutation.deserialize_json(
                data["addType"]
            )
        }
    elif data.get("updateType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_type_mutation

        return {
            "updateType": capo_bedrock.types.automated_reasoning_policy_update_type_mutation.deserialize_json(
                data["updateType"]
            )
        }
    elif data.get("deleteType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_mutation

        return {
            "deleteType": capo_bedrock.types.automated_reasoning_policy_delete_type_mutation.deserialize_json(
                data["deleteType"]
            )
        }
    elif data.get("addVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_mutation

        return {
            "addVariable": capo_bedrock.types.automated_reasoning_policy_add_variable_mutation.deserialize_json(
                data["addVariable"]
            )
        }
    elif data.get("updateVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_mutation

        return {
            "updateVariable": capo_bedrock.types.automated_reasoning_policy_update_variable_mutation.deserialize_json(
                data["updateVariable"]
            )
        }
    elif data.get("deleteVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation

        return {
            "deleteVariable": capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation.deserialize_json(
                data["deleteVariable"]
            )
        }
    elif data.get("addRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_mutation

        return {
            "addRule": capo_bedrock.types.automated_reasoning_policy_add_rule_mutation.deserialize_json(
                data["addRule"]
            )
        }
    elif data.get("updateRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_mutation

        return {
            "updateRule": capo_bedrock.types.automated_reasoning_policy_update_rule_mutation.deserialize_json(
                data["updateRule"]
            )
        }
    elif data.get("deleteRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation

        return {
            "deleteRule": capo_bedrock.types.automated_reasoning_policy_delete_rule_mutation.deserialize_json(
                data["deleteRule"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyMutation: no recognized variant key"
        )


def redact_sensitive(value: AutomatedReasoningPolicyMutation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "addType" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_type_mutation

        out["addType"] = (
            capo_bedrock.types.automated_reasoning_policy_add_type_mutation.redact_sensitive(
                value["addType"]
            )
        )
    if "updateType" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_type_mutation

        out["updateType"] = (
            capo_bedrock.types.automated_reasoning_policy_update_type_mutation.redact_sensitive(
                value["updateType"]
            )
        )
    if "deleteType" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_type_mutation

        out["deleteType"] = (
            capo_bedrock.types.automated_reasoning_policy_delete_type_mutation.redact_sensitive(
                value["deleteType"]
            )
        )
    if "addVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_variable_mutation

        out["addVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_add_variable_mutation.redact_sensitive(
                value["addVariable"]
            )
        )
    if "updateVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_variable_mutation

        out["updateVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_update_variable_mutation.redact_sensitive(
                value["updateVariable"]
            )
        )
    if "deleteVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation

        out["deleteVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_delete_variable_mutation.redact_sensitive(
                value["deleteVariable"]
            )
        )
    if "addRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_add_rule_mutation

        out["addRule"] = (
            capo_bedrock.types.automated_reasoning_policy_add_rule_mutation.redact_sensitive(
                value["addRule"]
            )
        )
    if "updateRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_update_rule_mutation

        out["updateRule"] = (
            capo_bedrock.types.automated_reasoning_policy_update_rule_mutation.redact_sensitive(
                value["updateRule"]
            )
        )
    return out
