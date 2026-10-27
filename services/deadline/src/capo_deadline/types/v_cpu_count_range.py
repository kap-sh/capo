"""Generated from Smithy shape ``com.amazonaws.deadline#VCpuCountRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.min_one_max_ten_thousand


class VCpuCountRange(TypedDict, closed=True):
    min: "capo_deadline.types.min_one_max_ten_thousand.MinOneMaxTenThousand"
    """The minimum amount of vCPU."""
    max: NotRequired[
        "capo_deadline.types.min_one_max_ten_thousand.MinOneMaxTenThousand"
    ]
    """The maximum amount of vCPU."""


# --- restJson1 ser/de ---
def serialize_json(value: VCpuCountRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> VCpuCountRange:
    out: VCpuCountRange = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    else:
        out["min"] = 0
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
