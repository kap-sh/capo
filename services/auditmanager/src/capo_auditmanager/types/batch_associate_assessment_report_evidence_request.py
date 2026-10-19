"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchAssociateAssessmentReportEvidenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.evidence_ids
    import capo_auditmanager.types.uuid


class BatchAssociateAssessmentReportEvidenceRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    evidence_folder_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the folder that the evidence is stored in. </p>"""
    evidence_ids: "capo_auditmanager.types.evidence_ids.EvidenceIds"
    """<p> The list of evidence identifiers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateAssessmentReportEvidenceRequest) -> dict:
    out: dict = {}
    out["evidenceFolderId"] = value["evidence_folder_id"]
    import capo_auditmanager.types.evidence_ids

    out["evidenceIds"] = capo_auditmanager.types.evidence_ids.serialize_json(
        value["evidence_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchAssociateAssessmentReportEvidenceRequest:
    out: BatchAssociateAssessmentReportEvidenceRequest = {}  # type: ignore[typeddict-item]
    if data.get("evidenceFolderId") is not None:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    else:
        out["evidence_folder_id"] = ""
    if data.get("evidenceIds") is not None:
        import capo_auditmanager.types.evidence_ids

        out["evidence_ids"] = capo_auditmanager.types.evidence_ids.deserialize_json(
            data["evidenceIds"]
        )
    else:
        out["evidence_ids"] = []
    return out
