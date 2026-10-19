"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_status
    import capo_auditmanager.types.uuid


class UpdateAssessmentStatusRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    status: "capo_auditmanager.types.assessment_status.AssessmentStatus"
    """<p> The current status of the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentStatusRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.assessment_status

    out["status"] = capo_auditmanager.types.assessment_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentStatusRequest:
    out: UpdateAssessmentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_auditmanager.types.assessment_status

        out["status"] = capo_auditmanager.types.assessment_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_auditmanager.types.assessment_status.AssessmentStatus", ""
        )
    return out
