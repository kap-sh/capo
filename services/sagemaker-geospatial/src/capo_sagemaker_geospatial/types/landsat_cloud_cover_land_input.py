"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LandsatCloudCoverLandInput``."""

from typing_extensions import TypedDict


class LandsatCloudCoverLandInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The minimum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover greater than or equal to this value.</p>"""
    upper_bound: "float"
    """<p>The maximum value for Land Cloud Cover property filter. This will filter items having Land Cloud Cover less than or equal to this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandsatCloudCoverLandInput) -> dict:
    out: dict = {}
    out["LowerBound"] = (
        "NaN"
        if value["lower_bound"] != value["lower_bound"]
        else "Infinity"
        if value["lower_bound"] == float("inf")
        else "-Infinity"
        if value["lower_bound"] == float("-inf")
        else value["lower_bound"]
    )
    out["UpperBound"] = (
        "NaN"
        if value["upper_bound"] != value["upper_bound"]
        else "Infinity"
        if value["upper_bound"] == float("inf")
        else "-Infinity"
        if value["upper_bound"] == float("-inf")
        else value["upper_bound"]
    )
    return out


def deserialize_json(data: dict) -> LandsatCloudCoverLandInput:
    out: LandsatCloudCoverLandInput = {}  # type: ignore[typeddict-item]
    if data.get("LowerBound") is not None:
        out["lower_bound"] = float(data["LowerBound"])
    else:
        out["lower_bound"] = 0.0
    if data.get("UpperBound") is not None:
        out["upper_bound"] = float(data["UpperBound"])
    else:
        out["upper_bound"] = 0.0
    return out
