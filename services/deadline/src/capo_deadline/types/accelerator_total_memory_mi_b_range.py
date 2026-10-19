"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorTotalMemoryMiBRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.min_zero_max_integer


class AcceleratorTotalMemoryMiBRange(TypedDict, closed=True):
    min: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The minimum amount of memory to use for the accelerator, measured in MiB.</p>"""
    max: NotRequired["capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"]
    """<p>The maximum amount of memory to use for the accelerator, measured in MiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorTotalMemoryMiBRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> AcceleratorTotalMemoryMiBRange:
    out: AcceleratorTotalMemoryMiBRange = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    else:
        out["min"] = 0
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
