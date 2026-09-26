"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#SubscriptionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.subscription_summary

SubscriptionSummaryList: TypeAlias = list[
    "capo_pricing_plan_manager.types.subscription_summary.SubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionSummaryList) -> list:
    import capo_pricing_plan_manager.types.subscription_summary

    out: list = []
    for item in value:
        out.append(
            capo_pricing_plan_manager.types.subscription_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionSummaryList:
    import capo_pricing_plan_manager.types.subscription_summary

    out: SubscriptionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pricing_plan_manager.types.subscription_summary.deserialize_json(item)
        )
    return out
