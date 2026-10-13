"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_description
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.assessment_reports_destination
    import capo_auditmanager.types.assessment_status
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.delegations
    import capo_auditmanager.types.roles
    import capo_auditmanager.types.scope
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class AssessmentMetadata(TypedDict, closed=True):
    name: NotRequired["capo_auditmanager.types.assessment_name.AssessmentName"]
    """<p> The name of the assessment. </p>"""
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.assessment_description.AssessmentDescription"
    ]
    """<p> The description of the assessment. </p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The name of the compliance standard that's related to the assessment, such as PCI-DSS. </p>"""
    status: NotRequired["capo_auditmanager.types.assessment_status.AssessmentStatus"]
    """<p> The overall status of the assessment. </p>"""
    assessment_reports_destination: NotRequired[
        "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The destination that evidence reports are stored in for the assessment. </p>"""
    scope: NotRequired["capo_auditmanager.types.scope.Scope"]
    """<p> The wrapper of Amazon Web Services accounts and services that are in scope for the assessment. </p>"""
    roles: NotRequired["capo_auditmanager.types.roles.Roles"]
    """<p> The roles that are associated with the assessment. </p>"""
    delegations: NotRequired["capo_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the assessment. </p>"""
    creation_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the assessment was created. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time of the most recent update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    if "status" in value:
        import capo_auditmanager.types.assessment_status

        out["status"] = capo_auditmanager.types.assessment_status.serialize_json(
            value["status"]
        )
    if "assessment_reports_destination" in value:
        import capo_auditmanager.types.assessment_reports_destination

        out["assessmentReportsDestination"] = (
            capo_auditmanager.types.assessment_reports_destination.serialize_json(
                value["assessment_reports_destination"]
            )
        )
    if "scope" in value:
        import capo_auditmanager.types.scope

        out["scope"] = capo_auditmanager.types.scope.serialize_json(value["scope"])
    if "roles" in value:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.serialize_json(value["roles"])
    if "delegations" in value:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    if "creation_time" in value:
        import capo_auditmanager.types.timestamp

        out["creationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentMetadata:
    out: AssessmentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    if data.get("status") is not None:
        import capo_auditmanager.types.assessment_status

        out["status"] = capo_auditmanager.types.assessment_status.deserialize_json(
            data["status"]
        )
    if data.get("assessmentReportsDestination") is not None:
        import capo_auditmanager.types.assessment_reports_destination

        out["assessment_reports_destination"] = (
            capo_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["assessmentReportsDestination"]
            )
        )
    if data.get("scope") is not None:
        import capo_auditmanager.types.scope

        out["scope"] = capo_auditmanager.types.scope.deserialize_json(data["scope"])
    if data.get("roles") is not None:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.deserialize_json(data["roles"])
    if data.get("delegations") is not None:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if data.get("creationTime") is not None:
        import capo_auditmanager.types.timestamp

        out["creation_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdated") is not None:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out


def redact_sensitive(value: AssessmentMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    if "assessment_reports_destination" in value:
        out["assessment_reports_destination"] = "*** Sensitive Data Redacted ***"
    if "scope" in value:
        out["scope"] = "*** Sensitive Data Redacted ***"
    if "roles" in value:
        out["roles"] = "*** Sensitive Data Redacted ***"
    if "delegations" in value:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.redact_sensitive(
            value["delegations"]
        )
    return out
