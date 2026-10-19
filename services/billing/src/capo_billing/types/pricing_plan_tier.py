"""Generated from Smithy shape ``com.amazonaws.billing#PricingPlanTier``."""

from typing_extensions import NotRequired, TypedDict


class PricingPlanTier(TypedDict, closed=True):
    tier_minimum: "str"
    """<p>The minimum spend threshold for this tier.</p>"""
    tier_maximum: NotRequired["str"]
    """<p>The maximum spend threshold for this tier.</p>"""
    base_charge: "str"
    """<p>The base charge for this tier.</p>"""
    additional_percentage_of_aggregate_charges: "str"
    """<p>The additional percentage applied to aggregate charges in this tier.</p>"""
    aggregate_charges_adjustment: "str"
    """<p>The adjustment applied to aggregate charges.</p>"""
    incremental: "bool"
    """<p>Whether the tier charges are calculated incrementally.</p>"""
    increment: NotRequired["str"]
    """<p>The increment amount for incremental tier calculations.</p>"""
    increment_charge: NotRequired["str"]
    """<p>The charge per increment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PricingPlanTier) -> dict:
    out: dict = {}
    out["tierMinimum"] = value["tier_minimum"]
    if "tier_maximum" in value:
        out["tierMaximum"] = value["tier_maximum"]
    out["baseCharge"] = value["base_charge"]
    out["additionalPercentageOfAggregateCharges"] = value[
        "additional_percentage_of_aggregate_charges"
    ]
    out["aggregateChargesAdjustment"] = value["aggregate_charges_adjustment"]
    out["incremental"] = value["incremental"]
    if "increment" in value:
        out["increment"] = value["increment"]
    if "increment_charge" in value:
        out["incrementCharge"] = value["increment_charge"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PricingPlanTier:
    out: PricingPlanTier = {}  # type: ignore[typeddict-item]
    if data.get("tierMinimum") is not None:
        out["tier_minimum"] = data["tierMinimum"]
    else:
        out["tier_minimum"] = ""
    if data.get("tierMaximum") is not None:
        out["tier_maximum"] = data["tierMaximum"]
    if data.get("baseCharge") is not None:
        out["base_charge"] = data["baseCharge"]
    else:
        out["base_charge"] = ""
    if data.get("additionalPercentageOfAggregateCharges") is not None:
        out["additional_percentage_of_aggregate_charges"] = data[
            "additionalPercentageOfAggregateCharges"
        ]
    else:
        out["additional_percentage_of_aggregate_charges"] = ""
    if data.get("aggregateChargesAdjustment") is not None:
        out["aggregate_charges_adjustment"] = data["aggregateChargesAdjustment"]
    else:
        out["aggregate_charges_adjustment"] = ""
    if data.get("incremental") is not None:
        out["incremental"] = data["incremental"]
    else:
        out["incremental"] = False
    if data.get("increment") is not None:
        out["increment"] = data["increment"]
    if data.get("incrementCharge") is not None:
        out["increment_charge"] = data["incrementCharge"]
    return out
