"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateHITReviewStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.entity_id


class UpdateHITReviewStatusRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p> The ID of the HIT to update. </p>"""
    revert: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> Specifies how to update the HIT status. Default is <code>False</code>. </p> <ul> <li> <p> Setting this to false will only transition a HIT from <code>Reviewable</code> to <code>Reviewing</code> </p> </li> <li> <p> Setting this to true will only transition a HIT from <code>Reviewing</code> to <code>Reviewable</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHITReviewStatusRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    if "revert" in value:
        out["Revert"] = value["revert"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHITReviewStatusRequest:
    out: UpdateHITReviewStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    if data.get("Revert") is not None:
        out["revert"] = data["Revert"]
    return out
