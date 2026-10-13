"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list
    import capo_bedrock.types.automated_reasoning_policy_scenario_expression


class AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation(
    TypedDict, closed=True
):
    rule_ids: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    ]
    """<p>The list of rule identifiers that were involved in the scenario being evaluated.</p>"""
    scenario_expression: "capo_bedrock.types.automated_reasoning_policy_scenario_expression.AutomatedReasoningPolicyScenarioExpression"
    """<p>The logical expression that defines the test scenario that generated this feedback.</p>"""
    feedback: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language.AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage"
    ]
    """<p>The feedback information about scenario performance, including any issues or improvements identified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation,
) -> dict:
    out: dict = {}
    if "rule_ids" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["ruleIds"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
                value["rule_ids"]
            )
        )
    out["scenarioExpression"] = value["scenario_expression"]
    if "feedback" in value:
        out["feedback"] = value["feedback"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation:
    out: AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("ruleIds") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    if data.get("scenarioExpression") is not None:
        out["scenario_expression"] = data["scenarioExpression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation.scenario_expression required"
        )
    if data.get("feedback") is not None:
        out["feedback"] = data["feedback"]
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scenario_expression" in value:
        out["scenario_expression"] = "*** Sensitive Data Redacted ***"
    if "feedback" in value:
        out["feedback"] = "*** Sensitive Data Redacted ***"
    return out
