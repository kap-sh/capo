"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionRule``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_alternate_expression
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_expression
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyDefinitionRule(TypedDict, closed=True):
    id: "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule within the policy.</p>"""
    expression: "capo_bedrock.types.automated_reasoning_policy_definition_rule_expression.AutomatedReasoningPolicyDefinitionRuleExpression"
    """<p>The formal logic expression of the rule.</p>"""
    alternate_expression: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_rule_alternate_expression.AutomatedReasoningPolicyDefinitionRuleAlternateExpression"
    ]
    """<p>The human-readable form of the rule expression, often in natural language or simplified notation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionRule) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["expression"] = value["expression"]
    if "alternate_expression" in value:
        out["alternateExpression"] = value["alternate_expression"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionRule:
    out: AutomatedReasoningPolicyDefinitionRule = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    if data.get("alternateExpression") is not None:
        out["alternate_expression"] = data["alternateExpression"]
    return out


def redact_sensitive(value: AutomatedReasoningPolicyDefinitionRule) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    if "alternate_expression" in value:
        out["alternate_expression"] = "*** Sensitive Data Redacted ***"
    return out
