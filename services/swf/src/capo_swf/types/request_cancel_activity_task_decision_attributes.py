"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelActivityTaskDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.activity_id


class RequestCancelActivityTaskDecisionAttributes(TypedDict, closed=True):
    activity_id: "capo_swf.types.activity_id.ActivityId"
    """<p>The <code>activityId</code> of the activity task to be canceled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestCancelActivityTaskDecisionAttributes) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestCancelActivityTaskDecisionAttributes:
    out: RequestCancelActivityTaskDecisionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        out["activity_id"] = ""
    return out
