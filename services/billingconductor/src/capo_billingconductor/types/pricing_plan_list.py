"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_list_element

PricingPlanList: TypeAlias = list[
    "capo_billingconductor.types.pricing_plan_list_element.PricingPlanListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanList) -> list:
    import capo_billingconductor.types.pricing_plan_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.pricing_plan_list_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PricingPlanList:
    import capo_billingconductor.types.pricing_plan_list_element

    out: PricingPlanList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billingconductor.types.pricing_plan_list_element.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PricingPlanList) -> list[Any]:
    import capo_billingconductor.types.pricing_plan_list_element

    return [
        capo_billingconductor.types.pricing_plan_list_element.redact_sensitive(item)
        for item in value
    ]
