"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyFidelityReport``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_accuracy_score
    import capo_bedrock.types.automated_reasoning_policy_coverage_score
    import capo_bedrock.types.automated_reasoning_policy_report_source_document_list
    import capo_bedrock.types.automated_reasoning_policy_rule_report_map
    import capo_bedrock.types.automated_reasoning_policy_variable_report_map


class AutomatedReasoningPolicyFidelityReport(TypedDict, closed=True):
    coverage_score: "capo_bedrock.types.automated_reasoning_policy_coverage_score.AutomatedReasoningPolicyCoverageScore"
    """<p>A score from 0.0 to 1.0 indicating how well the policy covers the statements in the source documents. A higher score means more of the source content is represented in the policy.</p>"""
    accuracy_score: "capo_bedrock.types.automated_reasoning_policy_accuracy_score.AutomatedReasoningPolicyAccuracyScore"
    """<p>A score from 0.0 to 1.0 indicating how accurate the policy rules are relative to the source documents. A higher score means the policy rules more faithfully represent the source material.</p>"""
    rule_reports: "capo_bedrock.types.automated_reasoning_policy_rule_report_map.AutomatedReasoningPolicyRuleReportMap"
    """<p>A mapping from rule identifiers to detailed fidelity reports for each rule, showing which source statements ground each rule and how accurate it is.</p>"""
    variable_reports: "capo_bedrock.types.automated_reasoning_policy_variable_report_map.AutomatedReasoningPolicyVariableReportMap"
    """<p>A mapping from variable names to detailed fidelity reports for each variable, showing which source statements ground each variable and how accurate it is.</p>"""
    document_sources: "capo_bedrock.types.automated_reasoning_policy_report_source_document_list.AutomatedReasoningPolicyReportSourceDocumentList"
    """<p>A list of source documents with their content broken down into atomic statements and annotated with line numbers for precise referencing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyFidelityReport) -> dict:
    out: dict = {}
    out["coverageScore"] = (
        "NaN"
        if value["coverage_score"] != value["coverage_score"]
        else "Infinity"
        if value["coverage_score"] == float("inf")
        else "-Infinity"
        if value["coverage_score"] == float("-inf")
        else value["coverage_score"]
    )
    out["accuracyScore"] = (
        "NaN"
        if value["accuracy_score"] != value["accuracy_score"]
        else "Infinity"
        if value["accuracy_score"] == float("inf")
        else "-Infinity"
        if value["accuracy_score"] == float("-inf")
        else value["accuracy_score"]
    )
    import capo_bedrock.types.automated_reasoning_policy_rule_report_map

    out["ruleReports"] = (
        capo_bedrock.types.automated_reasoning_policy_rule_report_map.serialize_json(
            value["rule_reports"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_variable_report_map

    out["variableReports"] = (
        capo_bedrock.types.automated_reasoning_policy_variable_report_map.serialize_json(
            value["variable_reports"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_report_source_document_list

    out["documentSources"] = (
        capo_bedrock.types.automated_reasoning_policy_report_source_document_list.serialize_json(
            value["document_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyFidelityReport:
    out: AutomatedReasoningPolicyFidelityReport = {}  # type: ignore[typeddict-item]
    if data.get("coverageScore") is not None:
        out["coverage_score"] = float(data["coverageScore"])
    else:
        out["coverage_score"] = 0.0
    if data.get("accuracyScore") is not None:
        out["accuracy_score"] = float(data["accuracyScore"])
    else:
        out["accuracy_score"] = 0.0
    if data.get("ruleReports") is not None:
        import capo_bedrock.types.automated_reasoning_policy_rule_report_map

        out["rule_reports"] = (
            capo_bedrock.types.automated_reasoning_policy_rule_report_map.deserialize_json(
                data["ruleReports"]
            )
        )
    else:
        out["rule_reports"] = {}
    if data.get("variableReports") is not None:
        import capo_bedrock.types.automated_reasoning_policy_variable_report_map

        out["variable_reports"] = (
            capo_bedrock.types.automated_reasoning_policy_variable_report_map.deserialize_json(
                data["variableReports"]
            )
        )
    else:
        out["variable_reports"] = {}
    if data.get("documentSources") is not None:
        import capo_bedrock.types.automated_reasoning_policy_report_source_document_list

        out["document_sources"] = (
            capo_bedrock.types.automated_reasoning_policy_report_source_document_list.deserialize_json(
                data["documentSources"]
            )
        )
    else:
        out["document_sources"] = []
    return out


def redact_sensitive(value: AutomatedReasoningPolicyFidelityReport) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rule_reports" in value:
        import capo_bedrock.types.automated_reasoning_policy_rule_report_map

        out["rule_reports"] = (
            capo_bedrock.types.automated_reasoning_policy_rule_report_map.redact_sensitive(
                value["rule_reports"]
            )
        )
    if "variable_reports" in value:
        out["variable_reports"] = "*** Sensitive Data Redacted ***"
    if "document_sources" in value:
        import capo_bedrock.types.automated_reasoning_policy_report_source_document_list

        out["document_sources"] = (
            capo_bedrock.types.automated_reasoning_policy_report_source_document_list.redact_sensitive(
                value["document_sources"]
            )
        )
    return out
