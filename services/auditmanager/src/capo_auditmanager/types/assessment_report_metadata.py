"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.assessment_report_description
    import capo_auditmanager.types.assessment_report_name
    import capo_auditmanager.types.assessment_report_status
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.username
    import capo_auditmanager.types.uuid


class AssessmentReportMetadata(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment report. </p>"""
    name: NotRequired[
        "capo_auditmanager.types.assessment_report_name.AssessmentReportName"
    ]
    """<p> The name of the assessment report. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.assessment_report_description.AssessmentReportDescription"
    ]
    """<p> The description of the assessment report. </p>"""
    assessment_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the associated assessment. </p>"""
    assessment_name: NotRequired[
        "capo_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p>The name of the associated assessment. </p>"""
    author: NotRequired["capo_auditmanager.types.username.Username"]
    """<p> The name of the user who created the assessment report. </p>"""
    status: NotRequired[
        "capo_auditmanager.types.assessment_report_status.AssessmentReportStatus"
    ]
    """<p> The current status of the assessment report. </p>"""
    creation_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the assessment report was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "author" in value:
        out["author"] = value["author"]
    if "status" in value:
        import capo_auditmanager.types.assessment_report_status

        out["status"] = capo_auditmanager.types.assessment_report_status.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import capo_auditmanager.types.timestamp

        out["creationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentReportMetadata:
    out: AssessmentReportMetadata = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("assessmentId") is not None:
        out["assessment_id"] = data["assessmentId"]
    if data.get("assessmentName") is not None:
        out["assessment_name"] = data["assessmentName"]
    if data.get("author") is not None:
        out["author"] = data["author"]
    if data.get("status") is not None:
        import capo_auditmanager.types.assessment_report_status

        out["status"] = (
            capo_auditmanager.types.assessment_report_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("creationTime") is not None:
        import capo_auditmanager.types.timestamp

        out["creation_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    return out


def redact_sensitive(value: AssessmentReportMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "assessment_name" in value:
        out["assessment_name"] = "*** Sensitive Data Redacted ***"
    if "author" in value:
        out["author"] = "*** Sensitive Data Redacted ***"
    return out
