"""Generated from Smithy shape ``com.amazonaws.connect#Threshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.comparison
    import capo_connect.types.threshold_value


class Threshold(TypedDict, closed=True):
    comparison: NotRequired["capo_connect.types.comparison.Comparison"]
    """<p>The type of comparison. Only "less than" (LT) comparisons are supported.</p>"""
    threshold_value: NotRequired["capo_connect.types.threshold_value.ThresholdValue"]
    """<p>The threshold value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threshold) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_connect.types.comparison

        out["Comparison"] = capo_connect.types.comparison.serialize_json(
            value["comparison"]
        )
    if "threshold_value" in value:
        out["ThresholdValue"] = (
            "NaN"
            if value["threshold_value"] != value["threshold_value"]
            else "Infinity"
            if value["threshold_value"] == float("inf")
            else "-Infinity"
            if value["threshold_value"] == float("-inf")
            else value["threshold_value"]
        )
    return out


def deserialize_json(data: dict) -> Threshold:
    out: Threshold = {}  # type: ignore[typeddict-item]
    if data.get("Comparison") is not None:
        import capo_connect.types.comparison

        out["comparison"] = capo_connect.types.comparison.deserialize_json(
            data["Comparison"]
        )
    if data.get("ThresholdValue") is not None:
        out["threshold_value"] = float(data["ThresholdValue"])
    return out
