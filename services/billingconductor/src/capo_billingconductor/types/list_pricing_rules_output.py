"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.pricing_rule_list
    import capo_billingconductor.types.token


class ListPricingRulesOutput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the described pricing rules are applicable. </p>"""
    pricing_rules: NotRequired[
        "capo_billingconductor.types.pricing_rule_list.PricingRuleList"
    ]
    """<p> A list containing the described pricing rules. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get pricing rules. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesOutput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "pricing_rules" in value:
        import capo_billingconductor.types.pricing_rule_list

        out["PricingRules"] = (
            capo_billingconductor.types.pricing_rule_list.serialize_json(
                value["pricing_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesOutput:
    out: ListPricingRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("PricingRules") is not None:
        import capo_billingconductor.types.pricing_rule_list

        out["pricing_rules"] = (
            capo_billingconductor.types.pricing_rule_list.deserialize_json(
                data["PricingRules"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListPricingRulesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pricing_rules" in value:
        import capo_billingconductor.types.pricing_rule_list

        out["pricing_rules"] = (
            capo_billingconductor.types.pricing_rule_list.redact_sensitive(
                value["pricing_rules"]
            )
        )
    return out
