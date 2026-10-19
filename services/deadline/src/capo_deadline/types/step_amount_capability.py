"""Generated from Smithy shape ``com.amazonaws.deadline#StepAmountCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.amount_capability_name
    import capo_deadline.types.double


class StepAmountCapability(TypedDict, closed=True):
    name: "capo_deadline.types.amount_capability_name.AmountCapabilityName"
    """<p>The name of the step.</p>"""
    min: NotRequired["capo_deadline.types.double.Double"]
    """<p>The minimum amount.</p>"""
    max: NotRequired["capo_deadline.types.double.Double"]
    """<p>The maximum amount.</p>"""
    value: NotRequired["capo_deadline.types.double.Double"]
    """<p>The amount value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "min" in value:
        out["min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "value" in value:
        out["value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    return out


def deserialize_json(data: dict) -> StepAmountCapability:
    out: StepAmountCapability = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("min") is not None:
        out["min"] = float(data["min"])
    if data.get("max") is not None:
        out["max"] = float(data["max"])
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    return out
