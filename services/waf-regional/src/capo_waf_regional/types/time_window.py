"""Generated from Smithy shape ``com.amazonaws.wafregional#TimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.timestamp


class TimeWindow(TypedDict, closed=True):
    start_time: "capo_waf_regional.types.timestamp.Timestamp"
    """<p>The beginning of the time range from which you want <code>GetSampledRequests</code> to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours.</p>"""
    end_time: "capo_waf_regional.types.timestamp.Timestamp"
    """<p>The end of the time range from which you want <code>GetSampledRequests</code> to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeWindow) -> dict:
    out: dict = {}
    import capo_waf_regional.types.timestamp

    out["StartTime"] = capo_waf_regional.types.timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_waf_regional.types.timestamp

    out["EndTime"] = capo_waf_regional.types.timestamp.serialize_aws_json_1_1(
        value["end_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeWindow:
    out: TimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_waf_regional.types.timestamp

        out["start_time"] = capo_waf_regional.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        raise DeserializationError("TimeWindow.start_time required")
    if data.get("EndTime") is not None:
        import capo_waf_regional.types.timestamp

        out["end_time"] = capo_waf_regional.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("TimeWindow.end_time required")
    return out
