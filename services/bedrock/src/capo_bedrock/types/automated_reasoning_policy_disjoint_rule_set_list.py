"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDisjointRuleSetList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set

AutomatedReasoningPolicyDisjointRuleSetList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set.AutomatedReasoningPolicyDisjointRuleSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDisjointRuleSetList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDisjointRuleSetList:
    import capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set

    out: AutomatedReasoningPolicyDisjointRuleSetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyDisjointRuleSetList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set

    return [
        capo_bedrock.types.automated_reasoning_policy_disjoint_rule_set.redact_sensitive(
            item
        )
        for item in value
    ]
