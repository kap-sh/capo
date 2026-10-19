"""Generated from Smithy shape ``com.amazonaws.swf#RecordMarkerDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.marker_name


class RecordMarkerDecisionAttributes(TypedDict, closed=True):
    marker_name: "capo_swf.types.marker_name.MarkerName"
    """<p> The name of the marker.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p> The details of the marker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordMarkerDecisionAttributes) -> dict:
    out: dict = {}
    out["markerName"] = value["marker_name"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecordMarkerDecisionAttributes:
    out: RecordMarkerDecisionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("markerName") is not None:
        out["marker_name"] = data["markerName"]
    else:
        out["marker_name"] = ""
    if data.get("details") is not None:
        out["details"] = data["details"]
    return out
