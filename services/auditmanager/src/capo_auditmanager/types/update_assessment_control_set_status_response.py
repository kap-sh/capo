"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlSetStatusResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_control_set


class UpdateAssessmentControlSetStatusResponse(TypedDict, closed=True):
    control_set: NotRequired[
        "capo_auditmanager.types.assessment_control_set.AssessmentControlSet"
    ]
    """<p> The name of the updated control set that the <code>UpdateAssessmentControlSetStatus</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlSetStatusResponse) -> dict:
    out: dict = {}
    if "control_set" in value:
        import capo_auditmanager.types.assessment_control_set

        out["controlSet"] = (
            capo_auditmanager.types.assessment_control_set.serialize_json(
                value["control_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlSetStatusResponse:
    out: UpdateAssessmentControlSetStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("controlSet") is not None:
        import capo_auditmanager.types.assessment_control_set

        out["control_set"] = (
            capo_auditmanager.types.assessment_control_set.deserialize_json(
                data["controlSet"]
            )
        )
    return out


def redact_sensitive(value: UpdateAssessmentControlSetStatusResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "control_set" in value:
        import capo_auditmanager.types.assessment_control_set

        out["control_set"] = (
            capo_auditmanager.types.assessment_control_set.redact_sensitive(
                value["control_set"]
            )
        )
    return out
