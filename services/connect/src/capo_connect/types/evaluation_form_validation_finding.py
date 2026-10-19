"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormValidationFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_validation_finding_description
    import capo_connect.types.evaluation_form_validation_finding_item_list
    import capo_connect.types.evaluation_form_validation_finding_severity
    import capo_connect.types.evaluation_form_validation_finding_suggestion
    import capo_connect.types.evaluation_form_validation_issue_code


class EvaluationFormValidationFinding(TypedDict, closed=True):
    issue_code: "capo_connect.types.evaluation_form_validation_issue_code.EvaluationFormValidationIssueCode"
    """<p>A code that identifies the type of validation issue found.</p>"""
    items: NotRequired[
        "capo_connect.types.evaluation_form_validation_finding_item_list.EvaluationFormValidationFindingItemList"
    ]
    """<p>A list of evaluation form items affected by this finding.</p>"""
    description: "capo_connect.types.evaluation_form_validation_finding_description.EvaluationFormValidationFindingDescription"
    """<p>A description of the validation issue.</p>"""
    suggestion: NotRequired[
        "capo_connect.types.evaluation_form_validation_finding_suggestion.EvaluationFormValidationFindingSuggestion"
    ]
    """<p>A suggested fix for the validation issue.</p>"""
    severity: "capo_connect.types.evaluation_form_validation_finding_severity.EvaluationFormValidationFindingSeverity"
    """<p>The severity of the finding. Valid values: <code>WARNING</code>, <code>ERROR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormValidationFinding) -> dict:
    out: dict = {}
    out["IssueCode"] = value["issue_code"]
    if "items" in value:
        import capo_connect.types.evaluation_form_validation_finding_item_list

        out["Items"] = (
            capo_connect.types.evaluation_form_validation_finding_item_list.serialize_json(
                value["items"]
            )
        )
    out["Description"] = value["description"]
    if "suggestion" in value:
        out["Suggestion"] = value["suggestion"]
    import capo_connect.types.evaluation_form_validation_finding_severity

    out["Severity"] = (
        capo_connect.types.evaluation_form_validation_finding_severity.serialize_json(
            value["severity"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormValidationFinding:
    out: EvaluationFormValidationFinding = {}  # type: ignore[typeddict-item]
    if data.get("IssueCode") is not None:
        out["issue_code"] = data["IssueCode"]
    else:
        out["issue_code"] = ""
    if data.get("Items") is not None:
        import capo_connect.types.evaluation_form_validation_finding_item_list

        out["items"] = (
            capo_connect.types.evaluation_form_validation_finding_item_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Suggestion") is not None:
        out["suggestion"] = data["Suggestion"]
    if data.get("Severity") is not None:
        import capo_connect.types.evaluation_form_validation_finding_severity

        out["severity"] = (
            capo_connect.types.evaluation_form_validation_finding_severity.deserialize_json(
                data["Severity"]
            )
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_connect.types.evaluation_form_validation_finding_severity.EvaluationFormValidationFindingSeverity",
            "",
        )
    return out
