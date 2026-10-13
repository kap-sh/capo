"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors


class BatchImportEvidenceToAssessmentControlResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors.BatchImportEvidenceToAssessmentControlErrors"
    ]
    """<p> A list of errors that the <code>BatchImportEvidenceToAssessmentControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors

        out["errors"] = (
            capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlResponse:
    out: BatchImportEvidenceToAssessmentControlResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors

        out["errors"] = (
            capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors.deserialize_json(
                data["errors"]
            )
        )
    return out


def redact_sensitive(
    value: BatchImportEvidenceToAssessmentControlResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors

        out["errors"] = (
            capo_auditmanager.types.batch_import_evidence_to_assessment_control_errors.redact_sensitive(
                value["errors"]
            )
        )
    return out
