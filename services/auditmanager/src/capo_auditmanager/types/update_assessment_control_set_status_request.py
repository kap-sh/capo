"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlSetStatusRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_status
    import capo_auditmanager.types.delegation_comment
    import capo_auditmanager.types.string
    import capo_auditmanager.types.uuid


class UpdateAssessmentControlSetStatusRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.string.String"
    """<p> The unique identifier for the control set. </p>"""
    status: "capo_auditmanager.types.control_set_status.ControlSetStatus"
    """<p> The status of the control set that's being updated. </p>"""
    comment: "capo_auditmanager.types.delegation_comment.DelegationComment"
    """<p> The comment that's related to the status update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlSetStatusRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.control_set_status

    out["status"] = capo_auditmanager.types.control_set_status.serialize_json(
        value["status"]
    )
    out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlSetStatusRequest:
    out: UpdateAssessmentControlSetStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_auditmanager.types.control_set_status

        out["status"] = capo_auditmanager.types.control_set_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentControlSetStatusRequest.status required"
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError(
            "UpdateAssessmentControlSetStatusRequest.comment required"
        )
    return out


def redact_sensitive(value: UpdateAssessmentControlSetStatusRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment" in value:
        out["comment"] = "*** Sensitive Data Redacted ***"
    return out
