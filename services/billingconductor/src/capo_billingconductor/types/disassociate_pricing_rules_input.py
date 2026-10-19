"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociatePricingRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_rule_arns_non_empty_input


class DisassociatePricingRulesInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>"""
    pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput"
    """<p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePricingRulesInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_billingconductor.types.pricing_rule_arns_non_empty_input

    out["PricingRuleArns"] = (
        capo_billingconductor.types.pricing_rule_arns_non_empty_input.serialize_json(
            value["pricing_rule_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociatePricingRulesInput:
    out: DisassociatePricingRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("PricingRuleArns") is not None:
        import capo_billingconductor.types.pricing_rule_arns_non_empty_input

        out["pricing_rule_arns"] = (
            capo_billingconductor.types.pricing_rule_arns_non_empty_input.deserialize_json(
                data["PricingRuleArns"]
            )
        )
    else:
        out["pricing_rule_arns"] = []
    return out
