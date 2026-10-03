"""Generated from Smithy shape ``com.amazonaws.connect#ThresholdV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.resource_arn_or_id
    import capo_connect.types.threshold_value


class ThresholdV2(TypedDict, closed=True):
    comparison: NotRequired["capo_connect.types.resource_arn_or_id.ResourceArnOrId"]
    """<p>The type of comparison. Currently, "less than" (LT), "less than equal" (LTE), and "greater than" (GT) comparisons are supported.</p>"""
    threshold_value: NotRequired["capo_connect.types.threshold_value.ThresholdValue"]
    """<p>The threshold value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdV2) -> dict:
    out: dict = {}
    if "comparison" in value:
        out["Comparison"] = value["comparison"]
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


def deserialize_json(data: dict) -> ThresholdV2:
    out: ThresholdV2 = {}  # type: ignore[typeddict-item]
    if data.get("Comparison") is not None:
        out["comparison"] = data["Comparison"]
    if data.get("ThresholdValue") is not None:
        out["threshold_value"] = float(data["ThresholdValue"])
    return out
