"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssociateAssessmentReportEvidenceFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.uuid


class AssociateAssessmentReportEvidenceFolderRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    evidence_folder_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the folder that the evidence is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAssessmentReportEvidenceFolderRequest) -> dict:
    out: dict = {}
    out["evidenceFolderId"] = value["evidence_folder_id"]
    return out


def deserialize_json(data: dict) -> AssociateAssessmentReportEvidenceFolderRequest:
    out: AssociateAssessmentReportEvidenceFolderRequest = {}  # type: ignore[typeddict-item]
    if data.get("evidenceFolderId") is not None:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    else:
        out["evidence_folder_id"] = ""
    return out
