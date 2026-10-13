"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_rule_list_element

PricingRuleList: TypeAlias = list[
    "capo_billingconductor.types.pricing_rule_list_element.PricingRuleListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleList) -> list:
    import capo_billingconductor.types.pricing_rule_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.pricing_rule_list_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PricingRuleList:
    import capo_billingconductor.types.pricing_rule_list_element

    out: PricingRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billingconductor.types.pricing_rule_list_element.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PricingRuleList) -> list[Any]:
    import capo_billingconductor.types.pricing_rule_list_element

    return [
        capo_billingconductor.types.pricing_rule_list_element.redact_sensitive(item)
        for item in value
    ]
