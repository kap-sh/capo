"""Generated from Smithy shape ``com.amazonaws.xray#ProbabilisticRuleValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_double


class ProbabilisticRuleValue(TypedDict, closed=True):
    desired_sampling_percentage: "capo_xray.types.nullable_double.NullableDouble"
    """<p> Configured sampling percentage of traceIds. Note that sampling can be subject to limits to ensure completeness of data. </p>"""
    actual_sampling_percentage: NotRequired[
        "capo_xray.types.nullable_double.NullableDouble"
    ]
    """<p> Applied sampling percentage of traceIds. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbabilisticRuleValue) -> dict:
    out: dict = {}
    out["DesiredSamplingPercentage"] = (
        "NaN"
        if value["desired_sampling_percentage"] != value["desired_sampling_percentage"]
        else "Infinity"
        if value["desired_sampling_percentage"] == float("inf")
        else "-Infinity"
        if value["desired_sampling_percentage"] == float("-inf")
        else value["desired_sampling_percentage"]
    )
    if "actual_sampling_percentage" in value:
        out["ActualSamplingPercentage"] = (
            "NaN"
            if value["actual_sampling_percentage"]
            != value["actual_sampling_percentage"]
            else "Infinity"
            if value["actual_sampling_percentage"] == float("inf")
            else "-Infinity"
            if value["actual_sampling_percentage"] == float("-inf")
            else value["actual_sampling_percentage"]
        )
    return out


def deserialize_json(data: dict) -> ProbabilisticRuleValue:
    out: ProbabilisticRuleValue = {}  # type: ignore[typeddict-item]
    if data.get("DesiredSamplingPercentage") is not None:
        out["desired_sampling_percentage"] = float(data["DesiredSamplingPercentage"])
    else:
        out["desired_sampling_percentage"] = 0.0
    if data.get("ActualSamplingPercentage") is not None:
        out["actual_sampling_percentage"] = float(data["ActualSamplingPercentage"])
    return out
