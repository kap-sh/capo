"""Generated from Smithy shape ``com.amazonaws.mturk#GetQualificationScoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id


class GetQualificationScoreRequest(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the QualificationType.</p>"""
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker whose Qualification is being updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQualificationScoreRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    out["WorkerId"] = value["worker_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQualificationScoreRequest:
    out: GetQualificationScoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        out["qualification_type_id"] = ""
    if data.get("WorkerId") is not None:
        out["worker_id"] = data["WorkerId"]
    else:
        out["worker_id"] = ""
    return out
