"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#StartTag``."""

from typing_extensions import NotRequired, TypedDict


class StartTag(TypedDict, closed=True):
    time_offset: "float"
    """<p>Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.</p>"""
    precise: NotRequired["bool"]
    """<p>Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTag) -> dict:
    out: dict = {}
    out["TimeOffset"] = (
        "NaN"
        if value["time_offset"] != value["time_offset"]
        else "Infinity"
        if value["time_offset"] == float("inf")
        else "-Infinity"
        if value["time_offset"] == float("-inf")
        else value["time_offset"]
    )
    if "precise" in value:
        out["Precise"] = value["precise"]
    return out


def deserialize_json(data: dict) -> StartTag:
    out: StartTag = {}  # type: ignore[typeddict-item]
    if data.get("TimeOffset") is not None:
        out["time_offset"] = float(data["TimeOffset"])
    else:
        out["time_offset"] = 0.0
    if data.get("Precise") is not None:
        out["precise"] = data["Precise"]
    return out
