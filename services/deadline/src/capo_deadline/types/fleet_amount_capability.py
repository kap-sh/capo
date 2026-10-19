"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAmountCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.amount_capability_name


class FleetAmountCapability(TypedDict, closed=True):
    name: "capo_deadline.types.amount_capability_name.AmountCapabilityName"
    """<p>The name of the fleet capability.</p>"""
    min: "float"
    """<p>The minimum amount of fleet worker capability.</p>"""
    max: NotRequired["float"]
    """<p>The maximum amount of the fleet worker capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    return out


def deserialize_json(data: dict) -> FleetAmountCapability:
    out: FleetAmountCapability = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("min") is not None:
        out["min"] = float(data["min"])
    else:
        out["min"] = 0.0
    if data.get("max") is not None:
        out["max"] = float(data["max"])
    return out
