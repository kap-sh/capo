"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.manual_evidence_list
    import capo_auditmanager.types.uuid


class BatchImportEvidenceToAssessmentControlRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId"
    """<p> The identifier for the control set. </p>"""
    control_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""
    manual_evidence: "capo_auditmanager.types.manual_evidence_list.ManualEvidenceList"
    """<p> The list of manual evidence objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.manual_evidence_list

    out["manualEvidence"] = capo_auditmanager.types.manual_evidence_list.serialize_json(
        value["manual_evidence"]
    )
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlRequest:
    out: BatchImportEvidenceToAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("manualEvidence") is not None:
        import capo_auditmanager.types.manual_evidence_list

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence_list.deserialize_json(
                data["manualEvidence"]
            )
        )
    else:
        out["manual_evidence"] = []
    return out


def redact_sensitive(
    value: BatchImportEvidenceToAssessmentControlRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "manual_evidence" in value:
        import capo_auditmanager.types.manual_evidence_list

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence_list.redact_sensitive(
                value["manual_evidence"]
            )
        )
    return out
