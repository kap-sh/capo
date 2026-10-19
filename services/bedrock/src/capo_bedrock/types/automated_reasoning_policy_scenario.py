"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenario``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list
    import capo_bedrock.types.automated_reasoning_policy_scenario_alternate_expression
    import capo_bedrock.types.automated_reasoning_policy_scenario_expression


class AutomatedReasoningPolicyScenario(TypedDict, closed=True):
    expression: "capo_bedrock.types.automated_reasoning_policy_scenario_expression.AutomatedReasoningPolicyScenarioExpression"
    """<p>The logical expression or condition that defines this test scenario.</p>"""
    alternate_expression: "capo_bedrock.types.automated_reasoning_policy_scenario_alternate_expression.AutomatedReasoningPolicyScenarioAlternateExpression"
    """<p>An alternative way to express the same test scenario, used for validation and comparison purposes.</p>"""
    expected_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    """<p>The expected outcome when this scenario is evaluated against the policy (e.g., PASS, FAIL, VIOLATION).</p>"""
    rule_ids: "capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    """<p>The list of rule identifiers that are expected to be triggered or evaluated by this test scenario.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenario) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    out["alternateExpression"] = value["alternate_expression"]
    import capo_bedrock.types.automated_reasoning_check_result

    out["expectedResult"] = (
        capo_bedrock.types.automated_reasoning_check_result.serialize_json(
            value["expected_result"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

    out["ruleIds"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
            value["rule_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyScenario:
    out: AutomatedReasoningPolicyScenario = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    if data.get("alternateExpression") is not None:
        out["alternate_expression"] = data["alternateExpression"]
    else:
        out["alternate_expression"] = ""
    if data.get("expectedResult") is not None:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expected_result"] = (
            capo_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedResult"]
            )
        )
    else:
        import typing

        out["expected_result"] = typing.cast(
            "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
            "",
        )
    if data.get("ruleIds") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    else:
        out["rule_ids"] = []
    return out


def redact_sensitive(value: AutomatedReasoningPolicyScenario) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    if "alternate_expression" in value:
        out["alternate_expression"] = "*** Sensitive Data Redacted ***"
    return out
