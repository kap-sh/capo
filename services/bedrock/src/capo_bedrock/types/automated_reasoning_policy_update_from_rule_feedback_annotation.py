"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list


class AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation(TypedDict, closed=True):
    rule_ids: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    ]
    """<p>The list of rule identifiers that the feedback applies to.</p>"""
    feedback: "capo_bedrock.types.automated_reasoning_policy_annotation_feedback_natural_language.AutomatedReasoningPolicyAnnotationFeedbackNaturalLanguage"
    """<p>The feedback information about rule performance, including suggestions for improvements or corrections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation,
) -> dict:
    out: dict = {}
    if "rule_ids" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["ruleIds"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
                value["rule_ids"]
            )
        )
    out["feedback"] = value["feedback"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation:
    out: AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("ruleIds") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    if data.get("feedback") is not None:
        out["feedback"] = data["feedback"]
    else:
        out["feedback"] = ""
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "feedback" in value:
        out["feedback"] = "*** Sensitive Data Redacted ***"
    return out
