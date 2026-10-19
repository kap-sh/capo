"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.metric_type
    import capo_codeguruprofiler.types.thread_states


class FrameMetric(TypedDict, closed=True):
    frame_name: "str"
    """<p> Name of the method common across the multiple occurrences of a frame in an application profile.</p>"""
    type: "capo_codeguruprofiler.types.metric_type.MetricType"
    """<p> A type of aggregation that specifies how a metric for a frame is analyzed. The supported value <code>AggregatedRelativeTotalTime</code> is an aggregation of the metric value for one frame that is calculated across the occurrences of all frames in a profile. </p>"""
    thread_states: "capo_codeguruprofiler.types.thread_states.ThreadStates"
    """<p>List of application runtime thread states used to get the counts for a frame a derive a metric value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetric) -> dict:
    out: dict = {}
    out["frameName"] = value["frame_name"]
    out["type"] = value["type"]
    import capo_codeguruprofiler.types.thread_states

    out["threadStates"] = capo_codeguruprofiler.types.thread_states.serialize_json(
        value["thread_states"]
    )
    return out


def deserialize_json(data: dict) -> FrameMetric:
    out: FrameMetric = {}  # type: ignore[typeddict-item]
    if data.get("frameName") is not None:
        out["frame_name"] = data["frameName"]
    else:
        out["frame_name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("threadStates") is not None:
        import capo_codeguruprofiler.types.thread_states

        out["thread_states"] = (
            capo_codeguruprofiler.types.thread_states.deserialize_json(
                data["threadStates"]
            )
        )
    else:
        out["thread_states"] = []
    return out
