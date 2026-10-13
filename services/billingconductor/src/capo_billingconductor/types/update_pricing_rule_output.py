"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingRuleOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_entity
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.modifier_percentage
    import capo_billingconductor.types.number_of_pricing_plans_associated_with
    import capo_billingconductor.types.operation
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.pricing_rule_description
    import capo_billingconductor.types.pricing_rule_name
    import capo_billingconductor.types.pricing_rule_scope
    import capo_billingconductor.types.pricing_rule_type
    import capo_billingconductor.types.service
    import capo_billingconductor.types.update_tiering_input
    import capo_billingconductor.types.usage_type


class UpdatePricingRuleOutput(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"]
    """<p> The Amazon Resource Name (ARN) of the successfully updated pricing rule. </p>"""
    name: NotRequired["capo_billingconductor.types.pricing_rule_name.PricingRuleName"]
    """<p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    scope: NotRequired[
        "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope"
    ]
    """<p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>"""
    type: NotRequired["capo_billingconductor.types.pricing_rule_type.PricingRuleType"]
    """<p> The new pricing rule type. </p>"""
    modifier_percentage: NotRequired[
        "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p> The new modifier to show pricing plan rates as a percentage. </p>"""
    service: NotRequired["capo_billingconductor.types.service.Service"]
    """<p> If the <code>Scope</code> attribute is set to <code>SERVICE</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>"""
    associated_pricing_plan_count: "capo_billingconductor.types.number_of_pricing_plans_associated_with.NumberOfPricingPlansAssociatedWith"
    """<p> The pricing plans count that this pricing rule is associated with. </p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p> The most recent time the pricing rule was modified. </p>"""
    billing_entity: NotRequired[
        "capo_billingconductor.types.billing_entity.BillingEntity"
    ]
    """<p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>"""
    tiering: NotRequired[
        "capo_billingconductor.types.update_tiering_input.UpdateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""
    usage_type: NotRequired["capo_billingconductor.types.usage_type.UsageType"]
    """<p>Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an <code>M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>"""
    operation: NotRequired["capo_billingconductor.types.operation.Operation"]
    """<p>Operation refers to the specific Amazon Web Services covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingRuleOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "scope" in value:
        import capo_billingconductor.types.pricing_rule_scope

        out["Scope"] = capo_billingconductor.types.pricing_rule_scope.serialize_json(
            value["scope"]
        )
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
    if "service" in value:
        out["Service"] = value["service"]
    out["AssociatedPricingPlanCount"] = value.get("associated_pricing_plan_count", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    if "billing_entity" in value:
        out["BillingEntity"] = value["billing_entity"]
    if "tiering" in value:
        import capo_billingconductor.types.update_tiering_input

        out["Tiering"] = (
            capo_billingconductor.types.update_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> UpdatePricingRuleOutput:
    out: UpdatePricingRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Scope") is not None:
        import capo_billingconductor.types.pricing_rule_scope

        out["scope"] = capo_billingconductor.types.pricing_rule_scope.deserialize_json(
            data["Scope"]
        )
    if data.get("Type") is not None:
        import capo_billingconductor.types.pricing_rule_type

        out["type"] = capo_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    if data.get("ModifierPercentage") is not None:
        out["modifier_percentage"] = float(data["ModifierPercentage"])
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("AssociatedPricingPlanCount") is not None:
        out["associated_pricing_plan_count"] = data["AssociatedPricingPlanCount"]
    else:
        out["associated_pricing_plan_count"] = 0
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("BillingEntity") is not None:
        out["billing_entity"] = data["BillingEntity"]
    if data.get("Tiering") is not None:
        import capo_billingconductor.types.update_tiering_input

        out["tiering"] = (
            capo_billingconductor.types.update_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    if data.get("UsageType") is not None:
        out["usage_type"] = data["UsageType"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    return out


def redact_sensitive(value: UpdatePricingRuleOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
