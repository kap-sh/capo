"""Generated from Smithy shape ``com.amazonaws.xray#Trace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_double
    import capo_xray.types.segment_list
    import capo_xray.types.trace_id


class Trace(TypedDict, closed=True):
    id: NotRequired["capo_xray.types.trace_id.TraceId"]
    """<p>The unique identifier for the request that generated the trace's segments and subsegments.</p>"""
    duration: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The length of time in seconds between the start time of the earliest segment that started and the end time of the last segment that completed.</p>"""
    limit_exceeded: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>LimitExceeded is set to true when the trace has exceeded the <code>Trace document size</code> limit. For more information about this limit and other X-Ray limits and quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/xray.html">Amazon Web Services X-Ray endpoints and quotas</a>.</p>"""
    segments: NotRequired["capo_xray.types.segment_list.SegmentList"]
    """<p>Segment documents for the segments and subsegments that comprise the trace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "duration" in value:
        out["Duration"] = (
            "NaN"
            if value["duration"] != value["duration"]
            else "Infinity"
            if value["duration"] == float("inf")
            else "-Infinity"
            if value["duration"] == float("-inf")
            else value["duration"]
        )
    if "limit_exceeded" in value:
        out["LimitExceeded"] = value["limit_exceeded"]
    if "segments" in value:
        import capo_xray.types.segment_list

        out["Segments"] = capo_xray.types.segment_list.serialize_json(value["segments"])
    return out


def deserialize_json(data: dict) -> Trace:
    out: Trace = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Duration") is not None:
        out["duration"] = float(data["Duration"])
    if data.get("LimitExceeded") is not None:
        out["limit_exceeded"] = data["LimitExceeded"]
    if data.get("Segments") is not None:
        import capo_xray.types.segment_list

        out["segments"] = capo_xray.types.segment_list.deserialize_json(
            data["Segments"]
        )
    return out
