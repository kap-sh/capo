"""Generated from Smithy shape ``com.amazonaws.appintegrations#OnDemandConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.non_blank_string


class OnDemandConfiguration(TypedDict, closed=True):
    start_time: "capo_appintegrations.types.non_blank_string.NonBlankString"
    """<p>The start time for data pull from the source as an Unix/epoch string in milliseconds</p>"""
    end_time: NotRequired["capo_appintegrations.types.non_blank_string.NonBlankString"]
    """<p>The end time for data pull from the source as an Unix/epoch string in milliseconds</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnDemandConfiguration) -> dict:
    out: dict = {}
    out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    return out


def deserialize_json(data: dict) -> OnDemandConfiguration:
    out: OnDemandConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = ""
    if data.get("EndTime") is not None:
        out["end_time"] = data["EndTime"]
    return out
