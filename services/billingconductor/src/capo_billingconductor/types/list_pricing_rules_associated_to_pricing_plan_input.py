"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesAssociatedToPricingPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.max_pricing_plan_results
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.token


class ListPricingRulesAssociatedToPricingPlanInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the pricing rule associations are to be listed. </p>"""
    pricing_plan_arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p> The Amazon Resource Name (ARN) of the pricing plan for which associations are to be listed.</p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
    ]
    """<p>The optional maximum number of pricing rule associations to retrieve.</p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The optional pagination token returned by a previous call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesAssociatedToPricingPlanInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["PricingPlanArn"] = value["pricing_plan_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingRulesAssociatedToPricingPlanInput:
    out: ListPricingRulesAssociatedToPricingPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("PricingPlanArn") is not None:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    else:
        out["pricing_plan_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
