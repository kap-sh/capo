"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_description
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.assessment_reports_destination
    import capo_auditmanager.types.roles
    import capo_auditmanager.types.scope
    import capo_auditmanager.types.uuid


class UpdateAssessmentRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    assessment_name: NotRequired[
        "capo_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the assessment to be updated. </p>"""
    assessment_description: NotRequired[
        "capo_auditmanager.types.assessment_description.AssessmentDescription"
    ]
    """<p> The description of the assessment. </p>"""
    scope: "capo_auditmanager.types.scope.Scope"
    """<p> The scope of the assessment. </p>"""
    assessment_reports_destination: NotRequired[
        "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The assessment report storage destination for the assessment that's being updated. </p>"""
    roles: NotRequired["capo_auditmanager.types.roles.Roles"]
    """<p> The list of roles for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentRequest) -> dict:
    out: dict = {}
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "assessment_description" in value:
        out["assessmentDescription"] = value["assessment_description"]
    import capo_auditmanager.types.scope

    out["scope"] = capo_auditmanager.types.scope.serialize_json(value["scope"])
    if "assessment_reports_destination" in value:
        import capo_auditmanager.types.assessment_reports_destination

        out["assessmentReportsDestination"] = (
            capo_auditmanager.types.assessment_reports_destination.serialize_json(
                value["assessment_reports_destination"]
            )
        )
    if "roles" in value:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.serialize_json(value["roles"])
    return out


def deserialize_json(data: dict) -> UpdateAssessmentRequest:
    out: UpdateAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentName") is not None:
        out["assessment_name"] = data["assessmentName"]
    if data.get("assessmentDescription") is not None:
        out["assessment_description"] = data["assessmentDescription"]
    if data.get("scope") is not None:
        import capo_auditmanager.types.scope

        out["scope"] = capo_auditmanager.types.scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("UpdateAssessmentRequest.scope required")
    if data.get("assessmentReportsDestination") is not None:
        import capo_auditmanager.types.assessment_reports_destination

        out["assessment_reports_destination"] = (
            capo_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["assessmentReportsDestination"]
            )
        )
    if data.get("roles") is not None:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.deserialize_json(data["roles"])
    return out


def redact_sensitive(value: UpdateAssessmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment_name" in value:
        out["assessment_name"] = "*** Sensitive Data Redacted ***"
    if "assessment_description" in value:
        out["assessment_description"] = "*** Sensitive Data Redacted ***"
    if "scope" in value:
        out["scope"] = "*** Sensitive Data Redacted ***"
    if "assessment_reports_destination" in value:
        out["assessment_reports_destination"] = "*** Sensitive Data Redacted ***"
    if "roles" in value:
        out["roles"] = "*** Sensitive Data Redacted ***"
    return out
