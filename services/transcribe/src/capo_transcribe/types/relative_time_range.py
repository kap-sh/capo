"""Generated from Smithy shape ``com.amazonaws.transcribe#RelativeTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.percentage


class RelativeTimeRange(TypedDict, closed=True):
    start_percentage: NotRequired["capo_transcribe.types.percentage.Percentage"]
    """<p>The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include <code>StartPercentage</code> in your request, you must also include <code>EndPercentage</code>.</p>"""
    end_percentage: NotRequired["capo_transcribe.types.percentage.Percentage"]
    """<p>The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include <code>EndPercentage</code> in your request, you must also include <code>StartPercentage</code>.</p>"""
    first: NotRequired["capo_transcribe.types.percentage.Percentage"]
    """<p>The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.</p>"""
    last: NotRequired["capo_transcribe.types.percentage.Percentage"]
    """<p>The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelativeTimeRange) -> dict:
    out: dict = {}
    if "start_percentage" in value:
        out["StartPercentage"] = value["start_percentage"]
    if "end_percentage" in value:
        out["EndPercentage"] = value["end_percentage"]
    if "first" in value:
        out["First"] = value["first"]
    if "last" in value:
        out["Last"] = value["last"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelativeTimeRange:
    out: RelativeTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("StartPercentage") is not None:
        out["start_percentage"] = data["StartPercentage"]
    if data.get("EndPercentage") is not None:
        out["end_percentage"] = data["EndPercentage"]
    if data.get("First") is not None:
        out["first"] = data["First"]
    if data.get("Last") is not None:
        out["last"] = data["Last"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelativeTimeRange) -> dict:
    out: dict = {}
    if "start_percentage" in value:
        out["StartPercentage"] = value["start_percentage"]
    if "end_percentage" in value:
        out["EndPercentage"] = value["end_percentage"]
    if "first" in value:
        out["First"] = value["first"]
    if "last" in value:
        out["Last"] = value["last"]
    return out


def deserialize_cbor(data: dict) -> RelativeTimeRange:
    out: RelativeTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("StartPercentage") is not None:
        out["start_percentage"] = data["StartPercentage"]
    if data.get("EndPercentage") is not None:
        out["end_percentage"] = data["EndPercentage"]
    if data.get("First") is not None:
        out["first"] = data["First"]
    if data.get("Last") is not None:
        out["last"] = data["Last"]
    return out
