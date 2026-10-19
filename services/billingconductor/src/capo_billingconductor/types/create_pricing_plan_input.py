"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_name
    import capo_billingconductor.types.pricing_rule_arns_input
    import capo_billingconductor.types.tag_map


class CreatePricingPlanInput(TypedDict, closed=True):
    client_token: NotRequired["capo_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "capo_billingconductor.types.pricing_plan_name.PricingPlanName"
    """<p>The name of the pricing plan. The names must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The description of the pricing plan. </p>"""
    pricing_rule_arns: NotRequired[
        "capo_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
    ]
    """<p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>"""
    tags: NotRequired["capo_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingPlanInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "pricing_rule_arns" in value:
        import capo_billingconductor.types.pricing_rule_arns_input

        out["PricingRuleArns"] = (
            capo_billingconductor.types.pricing_rule_arns_input.serialize_json(
                value["pricing_rule_arns"]
            )
        )
    if "tags" in value:
        import capo_billingconductor.types.tag_map

        out["Tags"] = capo_billingconductor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePricingPlanInput:
    out: CreatePricingPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PricingRuleArns") is not None:
        import capo_billingconductor.types.pricing_rule_arns_input

        out["pricing_rule_arns"] = (
            capo_billingconductor.types.pricing_rule_arns_input.deserialize_json(
                data["PricingRuleArns"]
            )
        )
    if data.get("Tags") is not None:
        import capo_billingconductor.types.tag_map

        out["tags"] = capo_billingconductor.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreatePricingPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
