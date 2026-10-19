"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingRuleInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_entity
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.create_tiering_input
    import capo_billingconductor.types.modifier_percentage
    import capo_billingconductor.types.operation
    import capo_billingconductor.types.pricing_rule_description
    import capo_billingconductor.types.pricing_rule_name
    import capo_billingconductor.types.pricing_rule_scope
    import capo_billingconductor.types.pricing_rule_type
    import capo_billingconductor.types.service
    import capo_billingconductor.types.tag_map
    import capo_billingconductor.types.usage_type


class CreatePricingRuleInput(TypedDict, closed=True):
    client_token: NotRequired["capo_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "capo_billingconductor.types.pricing_rule_name.PricingRuleName"
    """<p> The pricing rule name. The names must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The pricing rule description. </p>"""
    scope: "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope"
    """<p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>"""
    type: "capo_billingconductor.types.pricing_rule_type.PricingRuleType"
    """<p> The type of pricing rule. </p>"""
    modifier_percentage: NotRequired[
        "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p>A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.</p>"""
    service: NotRequired["capo_billingconductor.types.service.Service"]
    """<p> If the <code>Scope</code> attribute is set to <code>SERVICE</code> or <code>SKU</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>"""
    tags: NotRequired["capo_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a pricing rule. </p>"""
    billing_entity: NotRequired[
        "capo_billingconductor.types.billing_entity.BillingEntity"
    ]
    """<p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>"""
    tiering: NotRequired[
        "capo_billingconductor.types.create_tiering_input.CreateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""
    usage_type: NotRequired["capo_billingconductor.types.usage_type.UsageType"]
    """<p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>"""
    operation: NotRequired["capo_billingconductor.types.operation.Operation"]
    """<p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingRuleInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_billingconductor.types.pricing_rule_scope

    out["Scope"] = capo_billingconductor.types.pricing_rule_scope.serialize_json(
        value["scope"]
    )
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
    if "tags" in value:
        import capo_billingconductor.types.tag_map

        out["Tags"] = capo_billingconductor.types.tag_map.serialize_json(value["tags"])
    if "billing_entity" in value:
        out["BillingEntity"] = value["billing_entity"]
    if "tiering" in value:
        import capo_billingconductor.types.create_tiering_input

        out["Tiering"] = (
            capo_billingconductor.types.create_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> CreatePricingRuleInput:
    out: CreatePricingRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Scope") is not None:
        import capo_billingconductor.types.pricing_rule_scope

        out["scope"] = capo_billingconductor.types.pricing_rule_scope.deserialize_json(
            data["Scope"]
        )
    else:
        import typing

        out["scope"] = typing.cast(
            "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope", ""
        )
    if data.get("Type") is not None:
        import capo_billingconductor.types.pricing_rule_type

        out["type"] = capo_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_billingconductor.types.pricing_rule_type.PricingRuleType", ""
        )
    if data.get("ModifierPercentage") is not None:
        out["modifier_percentage"] = float(data["ModifierPercentage"])
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("Tags") is not None:
        import capo_billingconductor.types.tag_map

        out["tags"] = capo_billingconductor.types.tag_map.deserialize_json(data["Tags"])
    if data.get("BillingEntity") is not None:
        out["billing_entity"] = data["BillingEntity"]
    if data.get("Tiering") is not None:
        import capo_billingconductor.types.create_tiering_input

        out["tiering"] = (
            capo_billingconductor.types.create_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    if data.get("UsageType") is not None:
        out["usage_type"] = data["UsageType"]
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    return out


def redact_sensitive(value: CreatePricingRuleInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
