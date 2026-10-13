"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyVariableReport``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_accuracy_score
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name
    import capo_bedrock.types.automated_reasoning_policy_justification_list
    import capo_bedrock.types.automated_reasoning_policy_justification_text
    import capo_bedrock.types.automated_reasoning_policy_statement_reference_list


class AutomatedReasoningPolicyVariableReport(TypedDict, closed=True):
    policy_variable: "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the policy variable being analyzed in this report.</p>"""
    grounding_statements: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_statement_reference_list.AutomatedReasoningPolicyStatementReferenceList"
    ]
    """<p>References to statements from the source documents that provide the basis or justification for this variable.</p>"""
    grounding_justifications: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_justification_list.AutomatedReasoningPolicyJustificationList"
    ]
    """<p>Explanations describing how the source statements support and justify this specific variable definition.</p>"""
    accuracy_score: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_accuracy_score.AutomatedReasoningPolicyAccuracyScore"
    ]
    """<p>A score from 0.0 to 1.0 indicating how accurately this variable represents concepts from the source material.</p>"""
    accuracy_justification: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_justification_text.AutomatedReasoningPolicyJustificationText"
    ]
    """<p>A textual explanation of the accuracy score, describing why the variable received this particular accuracy rating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyVariableReport) -> dict:
    out: dict = {}
    out["policyVariable"] = value["policy_variable"]
    if "grounding_statements" in value:
        import capo_bedrock.types.automated_reasoning_policy_statement_reference_list

        out["groundingStatements"] = (
            capo_bedrock.types.automated_reasoning_policy_statement_reference_list.serialize_json(
                value["grounding_statements"]
            )
        )
    if "grounding_justifications" in value:
        import capo_bedrock.types.automated_reasoning_policy_justification_list

        out["groundingJustifications"] = (
            capo_bedrock.types.automated_reasoning_policy_justification_list.serialize_json(
                value["grounding_justifications"]
            )
        )
    if "accuracy_score" in value:
        out["accuracyScore"] = (
            "NaN"
            if value["accuracy_score"] != value["accuracy_score"]
            else "Infinity"
            if value["accuracy_score"] == float("inf")
            else "-Infinity"
            if value["accuracy_score"] == float("-inf")
            else value["accuracy_score"]
        )
    if "accuracy_justification" in value:
        out["accuracyJustification"] = value["accuracy_justification"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyVariableReport:
    out: AutomatedReasoningPolicyVariableReport = {}  # type: ignore[typeddict-item]
    if data.get("policyVariable") is not None:
        out["policy_variable"] = data["policyVariable"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyVariableReport.policy_variable required"
        )
    if data.get("groundingStatements") is not None:
        import capo_bedrock.types.automated_reasoning_policy_statement_reference_list

        out["grounding_statements"] = (
            capo_bedrock.types.automated_reasoning_policy_statement_reference_list.deserialize_json(
                data["groundingStatements"]
            )
        )
    if data.get("groundingJustifications") is not None:
        import capo_bedrock.types.automated_reasoning_policy_justification_list

        out["grounding_justifications"] = (
            capo_bedrock.types.automated_reasoning_policy_justification_list.deserialize_json(
                data["groundingJustifications"]
            )
        )
    if data.get("accuracyScore") is not None:
        out["accuracy_score"] = float(data["accuracyScore"])
    if data.get("accuracyJustification") is not None:
        out["accuracy_justification"] = data["accuracyJustification"]
    return out


def redact_sensitive(value: AutomatedReasoningPolicyVariableReport) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_variable" in value:
        out["policy_variable"] = "*** Sensitive Data Redacted ***"
    if "grounding_justifications" in value:
        import capo_bedrock.types.automated_reasoning_policy_justification_list

        out["grounding_justifications"] = (
            capo_bedrock.types.automated_reasoning_policy_justification_list.redact_sensitive(
                value["grounding_justifications"]
            )
        )
    if "accuracy_justification" in value:
        out["accuracy_justification"] = "*** Sensitive Data Redacted ***"
    return out
