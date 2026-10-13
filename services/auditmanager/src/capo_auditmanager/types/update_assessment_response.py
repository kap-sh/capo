"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment


class UpdateAssessmentResponse(TypedDict, closed=True):
    assessment: NotRequired["capo_auditmanager.types.assessment.Assessment"]
    """<p> The response object for the <code>UpdateAssessment</code> API. This is the name of the updated assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentResponse:
    out: UpdateAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessment") is not None:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out


def redact_sensitive(value: UpdateAssessmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.redact_sensitive(
            value["assessment"]
        )
    return out
