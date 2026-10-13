"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_name


class UpdatePricingPlanInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>"""
    name: NotRequired["capo_billingconductor.types.pricing_plan_name.PricingPlanName"]
    """<p>The name of the pricing plan. The name must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The description of the pricing plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanInput:
    out: UpdatePricingPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdatePricingPlanInput.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdatePricingPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
