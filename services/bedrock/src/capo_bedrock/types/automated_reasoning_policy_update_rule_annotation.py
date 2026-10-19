"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateRuleAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_expression
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyUpdateRuleAnnotation(TypedDict, closed=True):
    rule_id: "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule to update.</p>"""
    expression: "capo_bedrock.types.automated_reasoning_policy_definition_rule_expression.AutomatedReasoningPolicyDefinitionRuleExpression"
    """<p>The new formal logical expression for the rule, replacing the previous expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateRuleAnnotation) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateRuleAnnotation:
    out: AutomatedReasoningPolicyUpdateRuleAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateRuleAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
