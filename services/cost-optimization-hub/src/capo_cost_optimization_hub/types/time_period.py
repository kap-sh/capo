"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#TimePeriod``."""

from typing_extensions import TypedDict


class TimePeriod(TypedDict, closed=True):
    start: "str"
    """<p>The beginning of the time period (inclusive). Specify the date in ISO 8601 format, such as 2024-01-01.</p>"""
    end: "str"
    """<p>The end of the time period (exclusive). Specify the date in ISO 8601 format, such as 2024-12-31.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriod) -> dict:
    out: dict = {}
    out["start"] = value["start"]
    out["end"] = value["end"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        out["start"] = data["start"]
    else:
        out["start"] = ""
    if data.get("end") is not None:
        out["end"] = data["end"]
    else:
        out["end"] = ""
    return out
