"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingRuleInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.modifier_percentage
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.pricing_rule_description
    import capo_billingconductor.types.pricing_rule_name
    import capo_billingconductor.types.pricing_rule_type
    import capo_billingconductor.types.update_tiering_input


class UpdatePricingRuleInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    """<p> The Amazon Resource Name (ARN) of the pricing rule to update. </p>"""
    name: NotRequired["capo_billingconductor.types.pricing_rule_name.PricingRuleName"]
    """<p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    type: NotRequired["capo_billingconductor.types.pricing_rule_type.PricingRuleType"]
    """<p> The new pricing rule type. </p>"""
    modifier_percentage: NotRequired[
        "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p> The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places. </p>"""
    tiering: NotRequired[
        "capo_billingconductor.types.update_tiering_input.UpdateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingRuleInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_billingconductor.types.pricing_rule_type

        out["Type"] = capo_billingconductor.types.pricing_rule_type.serialize_json(
            value["type"]
        )
    if "modifier_percentage" in value:
        out["ModifierPercentage"] = (
            "NaN"
            if value["modifier_percentage"] != value["modifier_percentage"]
            else "Infinity"
            if value["modifier_percentage"] == float("inf")
            else "-Infinity"
            if value["modifier_percentage"] == float("-inf")
            else value["modifier_percentage"]
        )
    if "tiering" in value:
        import capo_billingconductor.types.update_tiering_input

        out["Tiering"] = (
            capo_billingconductor.types.update_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePricingRuleInput:
    out: UpdatePricingRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdatePricingRuleInput.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_billingconductor.types.pricing_rule_type

        out["type"] = capo_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    if data.get("ModifierPercentage") is not None:
        out["modifier_percentage"] = float(data["ModifierPercentage"])
    if data.get("Tiering") is not None:
        import capo_billingconductor.types.update_tiering_input

        out["tiering"] = (
            capo_billingconductor.types.update_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    return out


def redact_sensitive(value: UpdatePricingRuleInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
