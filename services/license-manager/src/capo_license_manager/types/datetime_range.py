"""Generated from Smithy shape ``com.amazonaws.licensemanager#DatetimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.iso8601_date_time


class DatetimeRange(TypedDict, closed=True):
    begin: "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    """<p>Start of the time range.</p>"""
    end: NotRequired["capo_license_manager.types.iso8601_date_time.ISO8601DateTime"]
    """<p>End of the time range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatetimeRange) -> dict:
    out: dict = {}
    out["Begin"] = value["begin"]
    if "end" in value:
        out["End"] = value["end"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatetimeRange:
    out: DatetimeRange = {}  # type: ignore[typeddict-item]
    if data.get("Begin") is not None:
        out["begin"] = data["Begin"]
    else:
        out["begin"] = ""
    if data.get("End") is not None:
        out["end"] = data["End"]
    return out
