"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.capacity_unit
    import capo_wafv2.types.custom_response_bodies
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.monetization_config
    import capo_wafv2.types.rules
    import capo_wafv2.types.scope
    import capo_wafv2.types.tag_list
    import capo_wafv2.types.visibility_config


class CreateRuleGroupRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    capacity: "capo_wafv2.types.capacity_unit.CapacityUnit"
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, WAF enforces this limit. You can check the capacity for a set of rules using <a>CheckCapacity</a>.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the rule group that helps with identification. </p>"""
    rules: NotRequired["capo_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    tags: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>An array of key:value pairs to associate with the resource.</p>"""
    custom_response_bodies: NotRequired[
        "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    """<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""
    monetization_config: NotRequired[
        "capo_wafv2.types.monetization_config.MonetizationConfig"
    ]
    """<p>The monetization configuration for the rule group. Provide this when any rule in the rule group uses the <code>Monetize</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Capacity"] = value["capacity"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import capo_wafv2.types.rules

        out["Rules"] = capo_wafv2.types.rules.serialize_aws_json_1_1(value["rules"])
    import capo_wafv2.types.visibility_config

    out["VisibilityConfig"] = capo_wafv2.types.visibility_config.serialize_aws_json_1_1(
        value["visibility_config"]
    )
    if "tags" in value:
        import capo_wafv2.types.tag_list

        out["Tags"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "custom_response_bodies" in value:
        import capo_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            capo_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    if "monetization_config" in value:
        import capo_wafv2.types.monetization_config

        out["MonetizationConfig"] = (
            capo_wafv2.types.monetization_config.serialize_aws_json_1_1(
                value["monetization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleGroupRequest:
    out: CreateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.name required")
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CreateRuleGroupRequest.scope required")
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.capacity required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rules") is not None:
        import capo_wafv2.types.rules

        out["rules"] = capo_wafv2.types.rules.deserialize_aws_json_1_1(data["Rules"])
    if data.get("VisibilityConfig") is not None:
        import capo_wafv2.types.visibility_config

        out["visibility_config"] = (
            capo_wafv2.types.visibility_config.deserialize_aws_json_1_1(
                data["VisibilityConfig"]
            )
        )
    else:
        raise DeserializationError("CreateRuleGroupRequest.visibility_config required")
    if data.get("Tags") is not None:
        import capo_wafv2.types.tag_list

        out["tags"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CustomResponseBodies") is not None:
        import capo_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            capo_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    if data.get("MonetizationConfig") is not None:
        import capo_wafv2.types.monetization_config

        out["monetization_config"] = (
            capo_wafv2.types.monetization_config.deserialize_aws_json_1_1(
                data["MonetizationConfig"]
            )
        )
    return out
