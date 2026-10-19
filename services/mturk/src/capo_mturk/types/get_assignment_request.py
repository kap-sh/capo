"""Generated from Smithy shape ``com.amazonaws.mturk#GetAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id


class GetAssignmentRequest(TypedDict, closed=True):
    assignment_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the Assignment to be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentId"] = value["assignment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssignmentRequest:
    out: GetAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssignmentId") is not None:
        out["assignment_id"] = data["AssignmentId"]
    else:
        out["assignment_id"] = ""
    return out
