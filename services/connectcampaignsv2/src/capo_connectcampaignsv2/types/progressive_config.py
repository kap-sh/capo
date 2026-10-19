"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ProgressiveConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.bandwidth_allocation


class ProgressiveConfig(TypedDict, closed=True):
    bandwidth_allocation: (
        "capo_connectcampaignsv2.types.bandwidth_allocation.BandwidthAllocation"
    )


# --- restJson1 ser/de ---
def serialize_json(value: ProgressiveConfig) -> dict:
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
    return out


def deserialize_json(data: dict) -> ProgressiveConfig:
    out: ProgressiveConfig = {}  # type: ignore[typeddict-item]
    if data.get("bandwidthAllocation") is not None:
        out["bandwidth_allocation"] = float(data["bandwidthAllocation"])
    else:
        out["bandwidth_allocation"] = 0.0
    return out
