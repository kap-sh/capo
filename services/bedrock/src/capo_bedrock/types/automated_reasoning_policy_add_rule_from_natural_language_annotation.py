"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_rule_natural_language


class AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation(
    TypedDict, closed=True
):
    natural_language: "capo_bedrock.types.automated_reasoning_policy_annotation_rule_natural_language.AutomatedReasoningPolicyAnnotationRuleNaturalLanguage"
    """<p>The natural language description of the rule that should be converted into a formal logical expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation,
) -> dict:
    out: dict = {}
    out["naturalLanguage"] = value["natural_language"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation:
    out: AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("naturalLanguage") is not None:
        out["natural_language"] = data["naturalLanguage"]
    else:
        out["natural_language"] = ""
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "natural_language" in value:
        out["natural_language"] = "*** Sensitive Data Redacted ***"
    return out
