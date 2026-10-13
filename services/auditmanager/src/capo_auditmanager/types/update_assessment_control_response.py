"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_control


class UpdateAssessmentControlResponse(TypedDict, closed=True):
    control: NotRequired["capo_auditmanager.types.assessment_control.AssessmentControl"]
    """<p> The name of the updated control set that the <code>UpdateAssessmentControl</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlResponse) -> dict:
    out: dict = {}
    if "control" in value:
        import capo_auditmanager.types.assessment_control

        out["control"] = capo_auditmanager.types.assessment_control.serialize_json(
            value["control"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlResponse:
    out: UpdateAssessmentControlResponse = {}  # type: ignore[typeddict-item]
    if data.get("control") is not None:
        import capo_auditmanager.types.assessment_control

        out["control"] = capo_auditmanager.types.assessment_control.deserialize_json(
            data["control"]
        )
    return out


def redact_sensitive(value: UpdateAssessmentControlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "control" in value:
        import capo_auditmanager.types.assessment_control

        out["control"] = capo_auditmanager.types.assessment_control.redact_sensitive(
            value["control"]
        )
    return out
