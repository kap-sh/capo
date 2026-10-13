"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentStatusResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment


class UpdateAssessmentStatusResponse(TypedDict, closed=True):
    assessment: NotRequired["capo_auditmanager.types.assessment.Assessment"]
    """<p> The name of the updated assessment that the <code>UpdateAssessmentStatus</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentStatusResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentStatusResponse:
    out: UpdateAssessmentStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out


def redact_sensitive(value: UpdateAssessmentStatusResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.redact_sensitive(
            value["assessment"]
        )
    return out
