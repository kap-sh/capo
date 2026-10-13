"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleListElement``."""

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
    import capo_billingconductor.types.tiering
    import capo_billingconductor.types.usage_type


class PricingRuleListElement(TypedDict, closed=True):
    name: NotRequired["capo_billingconductor.types.pricing_rule_name.PricingRuleName"]
    """<p>The name of a pricing rule.</p>"""
    arn: NotRequired["capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"]
    """<p>The Amazon Resource Name (ARN) used to uniquely identify a pricing rule.</p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p>The pricing rule description.</p>"""
    scope: NotRequired[
        "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope"
    ]
    """<p>The scope of pricing rule that indicates if it is globally applicable, or if it is service-specific.</p>"""
    type: NotRequired["capo_billingconductor.types.pricing_rule_type.PricingRuleType"]
    """<p>The type of pricing rule.</p>"""
    modifier_percentage: NotRequired[
        "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p>A percentage modifier applied on the public pricing rates.</p>"""
    service: NotRequired["capo_billingconductor.types.service.Service"]
    """<p>If the <code>Scope</code> attribute is <code>SERVICE</code>, this attribute indicates which service the <code>PricingRule</code> is applicable for.</p>"""
    associated_pricing_plan_count: "capo_billingconductor.types.number_of_pricing_plans_associated_with.NumberOfPricingPlansAssociatedWith"
    """<p>The pricing plans count that this pricing rule is associated with.</p>"""
    creation_time: "capo_billingconductor.types.instant.Instant"
    """<p>The time when the pricing rule was created.</p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p> The most recent time when the pricing rule was modified.</p>"""
    billing_entity: NotRequired[
        "capo_billingconductor.types.billing_entity.BillingEntity"
    ]
    """<p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>"""
    tiering: NotRequired["capo_billingconductor.types.tiering.Tiering"]
    """<p> The set of tiering configurations for the pricing rule. </p>"""
    usage_type: NotRequired["capo_billingconductor.types.usage_type.UsageType"]
    """<p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>"""
    operation: NotRequired["capo_billingconductor.types.operation.Operation"]
    """<p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleListElement) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    out["CreationTime"] = value.get("creation_time", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    if "billing_entity" in value:
        out["BillingEntity"] = value["billing_entity"]
    if "tiering" in value:
        import capo_billingconductor.types.tiering

        out["Tiering"] = capo_billingconductor.types.tiering.serialize_json(
            value["tiering"]
        )
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> PricingRuleListElement:
    out: PricingRuleListElement = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("BillingEntity") is not None:
        out["billing_entity"] = data["BillingEntity"]
    if data.get("Tiering") is not None:
        import capo_billingconductor.types.tiering

        out["tiering"] = capo_billingconductor.types.tiering.deserialize_json(
            data["Tiering"]
        )
    if data.get("UsageType") is not None:
        out["usage_type"] = data["UsageType"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    return out


def redact_sensitive(value: PricingRuleListElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
