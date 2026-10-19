"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDisjointRuleSet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list
    import capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list


class AutomatedReasoningPolicyDisjointRuleSet(TypedDict, closed=True):
    variables: "capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list.AutomatedReasoningPolicyDefinitionVariableNameList"
    """<p>The set of variables that are used by the rules in this disjoint set.</p>"""
    rules: "capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.AutomatedReasoningPolicyDisjointedRuleIdList"
    """<p>The list of rules that form this disjoint set, all operating on the same set of variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDisjointRuleSet) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list

    out["variables"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list.serialize_json(
            value["variables"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list

    out["rules"] = (
        capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.serialize_json(
            value["rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDisjointRuleSet:
    out: AutomatedReasoningPolicyDisjointRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("variables") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list

        out["variables"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list.deserialize_json(
                data["variables"]
            )
        )
    else:
        out["variables"] = []
    if data.get("rules") is not None:
        import capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list

        out["rules"] = (
            capo_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.deserialize_json(
                data["rules"]
            )
        )
    else:
        out["rules"] = []
    return out


def redact_sensitive(value: AutomatedReasoningPolicyDisjointRuleSet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "variables" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list

        out["variables"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable_name_list.redact_sensitive(
                value["variables"]
            )
        )
    return out
