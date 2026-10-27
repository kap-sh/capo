"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerAmountCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.amount_capability_name


class WorkerAmountCapability(TypedDict, closed=True):
    name: "capo_deadline.types.amount_capability_name.AmountCapabilityName"
    """The name of the worker amount capability."""
    value: "float"
    """The value of the worker amount capability."""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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


def deserialize_json(data: dict) -> WorkerAmountCapability:
    out: WorkerAmountCapability = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    return out
