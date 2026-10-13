"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.pricing_plan_list
    import capo_billingconductor.types.token


class ListPricingPlansOutput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the described pricing plans are applicable. </p>"""
    pricing_plans: NotRequired[
        "capo_billingconductor.types.pricing_plan_list.PricingPlanList"
    ]
    """<p>A list of <code>PricingPlanListElement</code> retrieved. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get pricing plans. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansOutput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "pricing_plans" in value:
        import capo_billingconductor.types.pricing_plan_list

        out["PricingPlans"] = (
            capo_billingconductor.types.pricing_plan_list.serialize_json(
                value["pricing_plans"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPricingPlansOutput:
    out: ListPricingPlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("PricingPlans") is not None:
        import capo_billingconductor.types.pricing_plan_list

        out["pricing_plans"] = (
            capo_billingconductor.types.pricing_plan_list.deserialize_json(
                data["PricingPlans"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListPricingPlansOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pricing_plans" in value:
        import capo_billingconductor.types.pricing_plan_list

        out["pricing_plans"] = (
            capo_billingconductor.types.pricing_plan_list.redact_sensitive(
                value["pricing_plans"]
            )
        )
    return out
