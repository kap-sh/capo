"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors


class BatchDeleteDelegationByAssessmentResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.BatchDeleteDelegationByAssessmentErrors"
    ]
    """<p> A list of errors that the <code>BatchDeleteDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteDelegationByAssessmentResponse:
    out: BatchDeleteDelegationByAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.deserialize_json(
                data["errors"]
            )
        )
    return out


def redact_sensitive(
    value: BatchDeleteDelegationByAssessmentResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        out["errors"] = "*** Sensitive Data Redacted ***"
    return out
