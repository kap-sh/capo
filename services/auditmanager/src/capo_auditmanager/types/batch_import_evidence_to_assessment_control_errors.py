"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlErrors``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_error

BatchImportEvidenceToAssessmentControlErrors: TypeAlias = list[
    "capo_auditmanager.types.batch_import_evidence_to_assessment_control_error.BatchImportEvidenceToAssessmentControlError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlErrors) -> list:
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_error

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.batch_import_evidence_to_assessment_control_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchImportEvidenceToAssessmentControlErrors:
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_error

    out: BatchImportEvidenceToAssessmentControlErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.batch_import_evidence_to_assessment_control_error.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BatchImportEvidenceToAssessmentControlErrors) -> list[Any]:
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_error

    return [
        capo_auditmanager.types.batch_import_evidence_to_assessment_control_error.redact_sensitive(
            item
        )
        for item in value
    ]
