"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_comment_body
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.control_status
    import capo_auditmanager.types.uuid


class UpdateAssessmentControlRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId"
    """<p> The unique identifier for the control set. </p>"""
    control_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the control. </p>"""
    control_status: NotRequired["capo_auditmanager.types.control_status.ControlStatus"]
    """<p> The status of the control. </p>"""
    comment_body: NotRequired[
        "capo_auditmanager.types.control_comment_body.ControlCommentBody"
    ]
    """<p> The comment body text for the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlRequest) -> dict:
    out: dict = {}
    if "control_status" in value:
        import capo_auditmanager.types.control_status

        out["controlStatus"] = capo_auditmanager.types.control_status.serialize_json(
            value["control_status"]
        )
    if "comment_body" in value:
        out["commentBody"] = value["comment_body"]
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlRequest:
    out: UpdateAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("controlStatus") is not None:
        import capo_auditmanager.types.control_status

        out["control_status"] = capo_auditmanager.types.control_status.deserialize_json(
            data["controlStatus"]
        )
    if data.get("commentBody") is not None:
        out["comment_body"] = data["commentBody"]
    return out


def redact_sensitive(value: UpdateAssessmentControlRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment_body" in value:
        out["comment_body"] = "*** Sensitive Data Redacted ***"
    return out
