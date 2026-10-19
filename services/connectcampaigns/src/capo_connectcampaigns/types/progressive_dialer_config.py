"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#ProgressiveDialerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.bandwidth_allocation
    import capo_connectcampaigns.types.dialing_capacity


class ProgressiveDialerConfig(TypedDict, closed=True):
    bandwidth_allocation: (
        "capo_connectcampaigns.types.bandwidth_allocation.BandwidthAllocation"
    )
    dialing_capacity: NotRequired[
        "capo_connectcampaigns.types.dialing_capacity.DialingCapacity"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ProgressiveDialerConfig) -> dict:
    out: dict = {}
    out["bandwidthAllocation"] = (
        "NaN"
        if value["bandwidth_allocation"] != value["bandwidth_allocation"]
        else "Infinity"
        if value["bandwidth_allocation"] == float("inf")
        else "-Infinity"
        if value["bandwidth_allocation"] == float("-inf")
        else value["bandwidth_allocation"]
    )
    if "dialing_capacity" in value:
        out["dialingCapacity"] = (
            "NaN"
            if value["dialing_capacity"] != value["dialing_capacity"]
            else "Infinity"
            if value["dialing_capacity"] == float("inf")
            else "-Infinity"
            if value["dialing_capacity"] == float("-inf")
            else value["dialing_capacity"]
        )
    return out


def deserialize_json(data: dict) -> ProgressiveDialerConfig:
    out: ProgressiveDialerConfig = {}  # type: ignore[typeddict-item]
    if data.get("bandwidthAllocation") is not None:
        out["bandwidth_allocation"] = float(data["bandwidthAllocation"])
    else:
        out["bandwidth_allocation"] = 0.0
    if data.get("dialingCapacity") is not None:
        out["dialing_capacity"] = float(data["dialingCapacity"])
    return out
