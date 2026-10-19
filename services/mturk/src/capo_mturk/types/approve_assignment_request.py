"""Generated from Smithy shape ``com.amazonaws.mturk#ApproveAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.entity_id
    import capo_mturk.types.string


class ApproveAssignmentRequest(TypedDict, closed=True):
    assignment_id: "capo_mturk.types.entity_id.EntityId"
    """<p> The ID of the assignment. The assignment must correspond to a HIT created by the Requester. </p>"""
    requester_feedback: NotRequired["capo_mturk.types.string.String"]
    """<p> A message for the Worker, which the Worker can see in the Status section of the web site. </p>"""
    override_rejection: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to <code>False</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApproveAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentId"] = value["assignment_id"]
    if "requester_feedback" in value:
        out["RequesterFeedback"] = value["requester_feedback"]
    if "override_rejection" in value:
        out["OverrideRejection"] = value["override_rejection"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApproveAssignmentRequest:
    out: ApproveAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssignmentId") is not None:
        out["assignment_id"] = data["AssignmentId"]
    else:
        out["assignment_id"] = ""
    if data.get("RequesterFeedback") is not None:
        out["requester_feedback"] = data["RequesterFeedback"]
    if data.get("OverrideRejection") is not None:
        out["override_rejection"] = data["OverrideRejection"]
    return out
