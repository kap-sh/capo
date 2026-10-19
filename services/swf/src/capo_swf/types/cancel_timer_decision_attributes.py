"""Generated from Smithy shape ``com.amazonaws.swf#CancelTimerDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.timer_id


class CancelTimerDecisionAttributes(TypedDict, closed=True):
    timer_id: "capo_swf.types.timer_id.TimerId"
    """<p> The unique ID of the timer to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelTimerDecisionAttributes) -> dict:
    out: dict = {}
    out["timerId"] = value["timer_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelTimerDecisionAttributes:
    out: CancelTimerDecisionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timerId") is not None:
        out["timer_id"] = data["timerId"]
    else:
        out["timer_id"] = ""
    return out
