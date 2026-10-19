"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteRuleAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyDeleteRuleAnnotation(TypedDict, closed=True):
    rule_id: "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule to delete from the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteRuleAnnotation) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteRuleAnnotation:
    out: AutomatedReasoningPolicyDeleteRuleAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    return out
