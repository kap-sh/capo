"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentReportsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_reports_metadata
    import capo_auditmanager.types.token


class ListAssessmentReportsResponse(TypedDict, closed=True):
    assessment_reports: NotRequired[
        "capo_auditmanager.types.assessment_reports_metadata.AssessmentReportsMetadata"
    ]
    """<p> The list of assessment reports that the <code>ListAssessmentReports</code> API returned. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentReportsResponse) -> dict:
    out: dict = {}
    if "assessment_reports" in value:
        import capo_auditmanager.types.assessment_reports_metadata

        out["assessmentReports"] = (
            capo_auditmanager.types.assessment_reports_metadata.serialize_json(
                value["assessment_reports"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentReportsResponse:
    out: ListAssessmentReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentReports") is not None:
        import capo_auditmanager.types.assessment_reports_metadata

        out["assessment_reports"] = (
            capo_auditmanager.types.assessment_reports_metadata.deserialize_json(
                data["assessmentReports"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAssessmentReportsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment_reports" in value:
        import capo_auditmanager.types.assessment_reports_metadata

        out["assessment_reports"] = (
            capo_auditmanager.types.assessment_reports_metadata.redact_sensitive(
                value["assessment_reports"]
            )
        )
    return out
