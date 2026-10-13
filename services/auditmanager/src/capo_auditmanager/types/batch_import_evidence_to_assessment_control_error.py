"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchImportEvidenceToAssessmentControlError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.error_code
    import capo_auditmanager.types.error_message
    import capo_auditmanager.types.manual_evidence


class BatchImportEvidenceToAssessmentControlError(TypedDict, closed=True):
    manual_evidence: NotRequired[
        "capo_auditmanager.types.manual_evidence.ManualEvidence"
    ]
    """<p> Manual evidence that can't be collected automatically by Audit Manager. </p>"""
    error_code: NotRequired["capo_auditmanager.types.error_code.ErrorCode"]
    """<p> The error code that the <code>BatchImportEvidenceToAssessmentControl</code> API returned. </p>"""
    error_message: NotRequired["capo_auditmanager.types.error_message.ErrorMessage"]
    """<p> The error message that the <code>BatchImportEvidenceToAssessmentControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportEvidenceToAssessmentControlError) -> dict:
    out: dict = {}
    if "manual_evidence" in value:
        import capo_auditmanager.types.manual_evidence

        out["manualEvidence"] = capo_auditmanager.types.manual_evidence.serialize_json(
            value["manual_evidence"]
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchImportEvidenceToAssessmentControlError:
    out: BatchImportEvidenceToAssessmentControlError = {}  # type: ignore[typeddict-item]
    if data.get("manualEvidence") is not None:
        import capo_auditmanager.types.manual_evidence

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence.deserialize_json(
                data["manualEvidence"]
            )
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


def redact_sensitive(
    value: BatchImportEvidenceToAssessmentControlError,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "manual_evidence" in value:
        import capo_auditmanager.types.manual_evidence

        out["manual_evidence"] = (
            capo_auditmanager.types.manual_evidence.redact_sensitive(
                value["manual_evidence"]
            )
        )
    return out
