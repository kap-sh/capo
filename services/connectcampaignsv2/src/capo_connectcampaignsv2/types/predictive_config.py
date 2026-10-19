"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PredictiveConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.bandwidth_allocation
    import capo_connectcampaignsv2.types.pacing_strategy_list


class PredictiveConfig(TypedDict, closed=True):
    bandwidth_allocation: (
        "capo_connectcampaignsv2.types.bandwidth_allocation.BandwidthAllocation"
    )
    pacing_strategies: NotRequired[
        "capo_connectcampaignsv2.types.pacing_strategy_list.PacingStrategyList"
    ]
    """Pacing strategies the dialer enforces simultaneously."""


# --- restJson1 ser/de ---
def serialize_json(value: PredictiveConfig) -> dict:
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
    if "pacing_strategies" in value:
        import capo_connectcampaignsv2.types.pacing_strategy_list

        out["pacingStrategies"] = (
            capo_connectcampaignsv2.types.pacing_strategy_list.serialize_json(
                value["pacing_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> PredictiveConfig:
    out: PredictiveConfig = {}  # type: ignore[typeddict-item]
    if data.get("bandwidthAllocation") is not None:
        out["bandwidth_allocation"] = float(data["bandwidthAllocation"])
    else:
        out["bandwidth_allocation"] = 0.0
    if data.get("pacingStrategies") is not None:
        import capo_connectcampaignsv2.types.pacing_strategy_list

        out["pacing_strategies"] = (
            capo_connectcampaignsv2.types.pacing_strategy_list.deserialize_json(
                data["pacingStrategies"]
            )
        )
    return out
