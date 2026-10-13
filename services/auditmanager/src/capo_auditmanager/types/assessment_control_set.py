"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControlSet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_controls
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.control_set_status
    import capo_auditmanager.types.delegations
    import capo_auditmanager.types.integer
    import capo_auditmanager.types.non_empty_string
    import capo_auditmanager.types.roles


class AssessmentControlSet(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.control_set_id.ControlSetId"]
    """<p> The identifier of the control set in the assessment. This is the control set name in a plain string format. </p>"""
    description: NotRequired["capo_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p> The description for the control set. </p>"""
    status: NotRequired["capo_auditmanager.types.control_set_status.ControlSetStatus"]
    """<p> The current status of the control set. </p>"""
    roles: NotRequired["capo_auditmanager.types.roles.Roles"]
    """<p> The roles that are associated with the control set. </p>"""
    controls: NotRequired[
        "capo_auditmanager.types.assessment_controls.AssessmentControls"
    ]
    """<p> The list of controls that's contained with the control set. </p>"""
    delegations: NotRequired["capo_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the control set. </p>"""
    system_evidence_count: "capo_auditmanager.types.integer.Integer"
    """<p> The total number of evidence objects that are retrieved automatically for the control set. </p>"""
    manual_evidence_count: "capo_auditmanager.types.integer.Integer"
    """<p> The total number of evidence objects that are uploaded manually to the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_auditmanager.types.control_set_status

        out["status"] = capo_auditmanager.types.control_set_status.serialize_json(
            value["status"]
        )
    if "roles" in value:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.serialize_json(value["roles"])
    if "controls" in value:
        import capo_auditmanager.types.assessment_controls

        out["controls"] = capo_auditmanager.types.assessment_controls.serialize_json(
            value["controls"]
        )
    if "delegations" in value:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    out["systemEvidenceCount"] = value.get("system_evidence_count", 0)
    out["manualEvidenceCount"] = value.get("manual_evidence_count", 0)
    return out


def deserialize_json(data: dict) -> AssessmentControlSet:
    out: AssessmentControlSet = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_auditmanager.types.control_set_status

        out["status"] = capo_auditmanager.types.control_set_status.deserialize_json(
            data["status"]
        )
    if data.get("roles") is not None:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.deserialize_json(data["roles"])
    if data.get("controls") is not None:
        import capo_auditmanager.types.assessment_controls

        out["controls"] = capo_auditmanager.types.assessment_controls.deserialize_json(
            data["controls"]
        )
    if data.get("delegations") is not None:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if data.get("systemEvidenceCount") is not None:
        out["system_evidence_count"] = data["systemEvidenceCount"]
    else:
        out["system_evidence_count"] = 0
    if data.get("manualEvidenceCount") is not None:
        out["manual_evidence_count"] = data["manualEvidenceCount"]
    else:
        out["manual_evidence_count"] = 0
    return out


def redact_sensitive(value: AssessmentControlSet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "roles" in value:
        out["roles"] = "*** Sensitive Data Redacted ***"
    if "controls" in value:
        import capo_auditmanager.types.assessment_controls

        out["controls"] = capo_auditmanager.types.assessment_controls.redact_sensitive(
            value["controls"]
        )
    if "delegations" in value:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.redact_sensitive(
            value["delegations"]
        )
    return out
