"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddRuleAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_expression


class AutomatedReasoningPolicyAddRuleAnnotation(TypedDict, closed=True):
    expression: "capo_bedrock.types.automated_reasoning_policy_definition_rule_expression.AutomatedReasoningPolicyDefinitionRuleExpression"
    """<p>The formal logical expression that defines the rule, using mathematical notation and referencing policy variables and types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddRuleAnnotation) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddRuleAnnotation:
    out: AutomatedReasoningPolicyAddRuleAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyAddRuleAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
