"""Generated from Smithy shape ``com.amazonaws.m2#HighAvailabilityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.capacity_value


class HighAvailabilityConfig(TypedDict, closed=True):
    desired_capacity: "capo_m2.types.capacity_value.CapacityValue"
    """<p>The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HighAvailabilityConfig) -> dict:
    out: dict = {}
    out["desiredCapacity"] = value["desired_capacity"]
    return out


def deserialize_json(data: dict) -> HighAvailabilityConfig:
    out: HighAvailabilityConfig = {}  # type: ignore[typeddict-item]
    if data.get("desiredCapacity") is not None:
        out["desired_capacity"] = data["desiredCapacity"]
    else:
        out["desired_capacity"] = 0
    return out
