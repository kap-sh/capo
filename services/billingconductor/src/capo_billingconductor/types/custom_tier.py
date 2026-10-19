"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomTier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_tier_begin_range_inclusive
    import capo_billingconductor.types.custom_tier_end_range_exclusive
    import capo_billingconductor.types.custom_tier_rate_value


class CustomTier(TypedDict, closed=True):
    begin_range_inclusive: "capo_billingconductor.types.custom_tier_begin_range_inclusive.CustomTierBeginRangeInclusive"
    """<p> The inclusive start of the usage range that this tier applies to. </p>"""
    end_range_exclusive: NotRequired[
        "capo_billingconductor.types.custom_tier_end_range_exclusive.CustomTierEndRangeExclusive"
    ]
    """<p> The exclusive end of the usage range that this tier applies to. If you don't specify a value, this tier applies to all usage that is greater than or equal to <code>BeginRangeInclusive</code>. </p>"""
    rate_value: "capo_billingconductor.types.custom_tier_rate_value.CustomTierRateValue"
    """<p> The rate that's applied to the usage that falls within this tier. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomTier) -> dict:
    out: dict = {}
    out["BeginRangeInclusive"] = (
        "NaN"
        if value["begin_range_inclusive"] != value["begin_range_inclusive"]
        else "Infinity"
        if value["begin_range_inclusive"] == float("inf")
        else "-Infinity"
        if value["begin_range_inclusive"] == float("-inf")
        else value["begin_range_inclusive"]
    )
    if "end_range_exclusive" in value:
        out["EndRangeExclusive"] = (
            "NaN"
            if value["end_range_exclusive"] != value["end_range_exclusive"]
            else "Infinity"
            if value["end_range_exclusive"] == float("inf")
            else "-Infinity"
            if value["end_range_exclusive"] == float("-inf")
            else value["end_range_exclusive"]
        )
    out["RateValue"] = (
        "NaN"
        if value["rate_value"] != value["rate_value"]
        else "Infinity"
        if value["rate_value"] == float("inf")
        else "-Infinity"
        if value["rate_value"] == float("-inf")
        else value["rate_value"]
    )
    return out


def deserialize_json(data: dict) -> CustomTier:
    out: CustomTier = {}  # type: ignore[typeddict-item]
    if data.get("BeginRangeInclusive") is not None:
        out["begin_range_inclusive"] = float(data["BeginRangeInclusive"])
    else:
        out["begin_range_inclusive"] = 0.0
    if data.get("EndRangeExclusive") is not None:
        out["end_range_exclusive"] = float(data["EndRangeExclusive"])
    if data.get("RateValue") is not None:
        out["rate_value"] = float(data["RateValue"])
    else:
        out["rate_value"] = 0.0
    return out
