"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment


class CreateAssessmentResponse(TypedDict, closed=True):
    assessment: NotRequired["capo_auditmanager.types.assessment.Assessment"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> CreateAssessmentResponse:
    out: CreateAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out


def redact_sensitive(value: CreateAssessmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.redact_sensitive(
            value["assessment"]
        )
    return out
