"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.metric_type
    import capo_codeguruprofiler.types.strings


class Metric(TypedDict, closed=True):
    frame_name: "str"
    """<p> The name of the method that appears as a frame in any stack in a profile. </p>"""
    type: "capo_codeguruprofiler.types.metric_type.MetricType"
    """<p> A type that specifies how a metric for a frame is analyzed. The supported value <code>AggregatedRelativeTotalTime</code> is an aggregation of the metric value for one frame that is calculated across the occurences of all frames in a profile.</p>"""
    thread_states: "capo_codeguruprofiler.types.strings.Strings"
    """<p> The list of application runtime thread states that is used to calculate the metric value for the frame. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metric) -> dict:
    out: dict = {}
    out["frameName"] = value["frame_name"]
    out["type"] = value["type"]
    import capo_codeguruprofiler.types.strings

    out["threadStates"] = capo_codeguruprofiler.types.strings.serialize_json(
        value["thread_states"]
    )
    return out


def deserialize_json(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if data.get("frameName") is not None:
        out["frame_name"] = data["frameName"]
    else:
        out["frame_name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("threadStates") is not None:
        import capo_codeguruprofiler.types.strings

        out["thread_states"] = capo_codeguruprofiler.types.strings.deserialize_json(
            data["threadStates"]
        )
    else:
        out["thread_states"] = []
    return out
