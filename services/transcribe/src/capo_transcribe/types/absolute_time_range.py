"""Generated from Smithy shape ``com.amazonaws.transcribe#AbsoluteTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.timestamp_milliseconds


class AbsoluteTimeRange(TypedDict, closed=True):
    start_time: NotRequired[
        "capo_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include <code>StartTime</code> in your request, you must also include <code>EndTime</code>.</p>"""
    end_time: NotRequired[
        "capo_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include <code>EndTime</code> in your request, you must also include <code>StartTime</code>.</p>"""
    first: NotRequired[
        "capo_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.</p>"""
    last: NotRequired[
        "capo_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AbsoluteTimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "first" in value:
        out["First"] = value["first"]
    if "last" in value:
        out["Last"] = value["last"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AbsoluteTimeRange:
    out: AbsoluteTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    if data.get("EndTime") is not None:
        out["end_time"] = data["EndTime"]
    if data.get("First") is not None:
        out["first"] = data["First"]
    if data.get("Last") is not None:
        out["last"] = data["Last"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AbsoluteTimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "first" in value:
        out["First"] = value["first"]
    if "last" in value:
        out["Last"] = value["last"]
    return out


def deserialize_cbor(data: dict) -> AbsoluteTimeRange:
    out: AbsoluteTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    if data.get("EndTime") is not None:
        out["end_time"] = data["EndTime"]
    if data.get("First") is not None:
        out["first"] = data["First"]
    if data.get("Last") is not None:
        out["last"] = data["Last"]
    return out
