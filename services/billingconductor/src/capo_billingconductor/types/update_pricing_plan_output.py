"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingPlanOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.number_of_associated_pricing_rules
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_name


class UpdatePricingPlanOutput(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p>The Amazon Resource Name (ARN) of the updated pricing plan. </p>"""
    name: NotRequired["capo_billingconductor.types.pricing_plan_name.PricingPlanName"]
    """<p> The name of the pricing plan. The name must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    size: "capo_billingconductor.types.number_of_associated_pricing_rules.NumberOfAssociatedPricingRules"
    """<p> The pricing rules count that's currently associated with this pricing plan list. </p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p> The most recent time when the pricing plan was modified. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Size"] = value.get("size", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanOutput:
    out: UpdatePricingPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out


def redact_sensitive(value: UpdatePricingPlanOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
