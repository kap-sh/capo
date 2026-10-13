"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanListElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.number_of_associated_pricing_rules
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_name


class PricingPlanListElement(TypedDict, closed=True):
    name: NotRequired["capo_billingconductor.types.pricing_plan_name.PricingPlanName"]
    """<p>The name of a pricing plan.</p>"""
    arn: NotRequired["capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p>The pricing plan Amazon Resource Names (ARN). This can be used to uniquely identify a pricing plan.</p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The pricing plan description.</p>"""
    size: "capo_billingconductor.types.number_of_associated_pricing_rules.NumberOfAssociatedPricingRules"
    """<p>The pricing rules count that's currently associated with this pricing plan list element.</p>"""
    creation_time: "capo_billingconductor.types.instant.Instant"
    """<p>The time when the pricing plan was created.</p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p>The most recent time when the pricing plan was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanListElement) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Size"] = value.get("size", 0)
    out["CreationTime"] = value.get("creation_time", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> PricingPlanListElement:
    out: PricingPlanListElement = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out


def redact_sensitive(value: PricingPlanListElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
