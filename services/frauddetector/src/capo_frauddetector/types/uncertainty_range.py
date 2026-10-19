"""Generated from Smithy shape ``com.amazonaws.frauddetector#UncertaintyRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float


class UncertaintyRange(TypedDict, closed=True):
    lower_bound_value: "capo_frauddetector.types.float.float"
    """<p> The lower bound value of the area under curve (auc). </p>"""
    upper_bound_value: "capo_frauddetector.types.float.float"
    """<p> The upper bound value of the area under curve (auc). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UncertaintyRange) -> dict:
    out: dict = {}
    out["lowerBoundValue"] = (
        "NaN"
        if value["lower_bound_value"] != value["lower_bound_value"]
        else "Infinity"
        if value["lower_bound_value"] == float("inf")
        else "-Infinity"
        if value["lower_bound_value"] == float("-inf")
        else value["lower_bound_value"]
    )
    out["upperBoundValue"] = (
        "NaN"
        if value["upper_bound_value"] != value["upper_bound_value"]
        else "Infinity"
        if value["upper_bound_value"] == float("inf")
        else "-Infinity"
        if value["upper_bound_value"] == float("-inf")
        else value["upper_bound_value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UncertaintyRange:
    out: UncertaintyRange = {}  # type: ignore[typeddict-item]
    if data.get("lowerBoundValue") is not None:
        out["lower_bound_value"] = float(data["lowerBoundValue"])
    else:
        out["lower_bound_value"] = 0.0
    if data.get("upperBoundValue") is not None:
        out["upper_bound_value"] = float(data["upperBoundValue"])
    else:
        out["upper_bound_value"] = 0.0
    return out
