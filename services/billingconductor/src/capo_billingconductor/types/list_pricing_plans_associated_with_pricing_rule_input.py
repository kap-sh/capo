"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansAssociatedWithPricingRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.max_pricing_rule_results
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.token


class ListPricingPlansAssociatedWithPricingRuleInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The pricing plan billing period for which associations will be listed. </p>"""
    pricing_rule_arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    """<p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
    ]
    """<p> The optional maximum number of pricing rule associations to retrieve. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The optional pagination token returned by a previous call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansAssociatedWithPricingRuleInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["PricingRuleArn"] = value["pricing_rule_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingPlansAssociatedWithPricingRuleInput:
    out: ListPricingPlansAssociatedWithPricingRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("PricingRuleArn") is not None:
        out["pricing_rule_arn"] = data["PricingRuleArn"]
    else:
        out["pricing_rule_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
