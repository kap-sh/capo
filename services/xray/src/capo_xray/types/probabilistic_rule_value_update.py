"""Generated from Smithy shape ``com.amazonaws.xray#ProbabilisticRuleValueUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_double


class ProbabilisticRuleValueUpdate(TypedDict, closed=True):
    desired_sampling_percentage: "capo_xray.types.nullable_double.NullableDouble"
    """<p> Configured sampling percentage of traceIds. Note that sampling can be subject to limits to ensure completeness of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbabilisticRuleValueUpdate) -> dict:
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
    return out


def deserialize_json(data: dict) -> ProbabilisticRuleValueUpdate:
    out: ProbabilisticRuleValueUpdate = {}  # type: ignore[typeddict-item]
    if data.get("DesiredSamplingPercentage") is not None:
        out["desired_sampling_percentage"] = float(data["DesiredSamplingPercentage"])
    else:
        out["desired_sampling_percentage"] = 0.0
    return out
