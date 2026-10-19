"""Generated from Smithy shape ``com.amazonaws.billing#PricingPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.pricing_plan_tier_list


class PricingPlan(TypedDict, closed=True):
    pricing_plan_id: NotRequired["str"]
    """<p>The unique identifier for the pricing plan.</p>"""
    name: NotRequired["str"]
    """<p>The name of the pricing plan.</p>"""
    description: NotRequired["str"]
    """<p>A description of the pricing plan.</p>"""
    start_date: NotRequired["datetime.datetime"]
    """<p>The start date of the pricing plan.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The end date of the pricing plan.</p>"""
    plan_discount_percent: NotRequired["str"]
    """<p>The discount percentage applied by this pricing plan.</p>"""
    discount_applies_to_minimum_charge: NotRequired["bool"]
    """<p>Whether the discount applies to the minimum Support charge.</p>"""
    minimum_charge: NotRequired["str"]
    """<p>The minimum Support charge amount for this pricing plan.</p>"""
    tiered: NotRequired["str"]
    """<p>Whether the pricing plan uses tiered pricing.</p>"""
    tiers: "capo_billing.types.pricing_plan_tier_list.PricingPlanTierList"
    """<p>The pricing tiers within this plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PricingPlan) -> dict:
    out: dict = {}
    if "pricing_plan_id" in value:
        out["pricingPlanId"] = value["pricing_plan_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["startDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "plan_discount_percent" in value:
        out["planDiscountPercent"] = value["plan_discount_percent"]
    if "discount_applies_to_minimum_charge" in value:
        out["discountAppliesToMinimumCharge"] = value[
            "discount_applies_to_minimum_charge"
        ]
    if "minimum_charge" in value:
        out["minimumCharge"] = value["minimum_charge"]
    if "tiered" in value:
        out["tiered"] = value["tiered"]
    import capo_billing.types.pricing_plan_tier_list

    out["tiers"] = capo_billing.types.pricing_plan_tier_list.serialize_aws_json_1_0(
        value["tiers"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PricingPlan:
    out: PricingPlan = {}  # type: ignore[typeddict-item]
    if data.get("pricingPlanId") is not None:
        out["pricing_plan_id"] = data["pricingPlanId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("startDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    if data.get("endDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    if data.get("planDiscountPercent") is not None:
        out["plan_discount_percent"] = data["planDiscountPercent"]
    if data.get("discountAppliesToMinimumCharge") is not None:
        out["discount_applies_to_minimum_charge"] = data[
            "discountAppliesToMinimumCharge"
        ]
    if data.get("minimumCharge") is not None:
        out["minimum_charge"] = data["minimumCharge"]
    if data.get("tiered") is not None:
        out["tiered"] = data["tiered"]
    if data.get("tiers") is not None:
        import capo_billing.types.pricing_plan_tier_list

        out["tiers"] = (
            capo_billing.types.pricing_plan_tier_list.deserialize_aws_json_1_0(
                data["tiers"]
            )
        )
    else:
        out["tiers"] = []
    return out
