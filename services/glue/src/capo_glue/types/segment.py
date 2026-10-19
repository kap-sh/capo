"""Generated from Smithy shape ``com.amazonaws.glue#Segment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.non_negative_integer
    import capo_glue.types.total_segments_integer


class Segment(TypedDict, closed=True):
    segment_number: "capo_glue.types.non_negative_integer.NonNegativeInteger"
    """<p>The zero-based index number of the segment. For example, if the total number of segments is 4, <code>SegmentNumber</code> values range from 0 through 3.</p>"""
    total_segments: "capo_glue.types.total_segments_integer.TotalSegmentsInteger"
    """<p>The total number of segments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Segment) -> dict:
    out: dict = {}
    out["SegmentNumber"] = value.get("segment_number", 0)
    out["TotalSegments"] = value["total_segments"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Segment:
    out: Segment = {}  # type: ignore[typeddict-item]
    if data.get("SegmentNumber") is not None:
        out["segment_number"] = data["SegmentNumber"]
    else:
        out["segment_number"] = 0
    if data.get("TotalSegments") is not None:
        out["total_segments"] = data["TotalSegments"]
    else:
        out["total_segments"] = 0
    return out
