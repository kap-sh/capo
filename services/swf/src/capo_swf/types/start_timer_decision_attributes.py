"""Generated from Smithy shape ``com.amazonaws.swf#StartTimerDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds
    import capo_swf.types.timer_id


class StartTimerDecisionAttributes(TypedDict, closed=True):
    timer_id: "capo_swf.types.timer_id.TimerId"
    r"""<p> The unique ID of the timer.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>The data attached to the event that can be used by the decider in subsequent workflow tasks.</p>"""
    start_to_fire_timeout: "capo_swf.types.duration_in_seconds.DurationInSeconds"
    """<p> The duration to wait before firing the timer.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartTimerDecisionAttributes) -> dict:
    out: dict = {}
    out["timerId"] = value["timer_id"]
    if "control" in value:
        out["control"] = value["control"]
    out["startToFireTimeout"] = value["start_to_fire_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartTimerDecisionAttributes:
    out: StartTimerDecisionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timerId") is not None:
        out["timer_id"] = data["timerId"]
    else:
        out["timer_id"] = ""
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("startToFireTimeout") is not None:
        out["start_to_fire_timeout"] = data["startToFireTimeout"]
    else:
        out["start_to_fire_timeout"] = ""
    return out
