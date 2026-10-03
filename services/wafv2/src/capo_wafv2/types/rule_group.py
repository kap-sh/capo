"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.capacity_unit
    import capo_wafv2.types.custom_response_bodies
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.label_name
    import capo_wafv2.types.label_summaries
    import capo_wafv2.types.monetization_config
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.rules
    import capo_wafv2.types.visibility_config


class RuleGroup(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    id: "capo_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    capacity: "capo_wafv2.types.capacity_unit.CapacityUnit"
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, WAF enforces this limit. You can check the capacity for a set of rules using <a>CheckCapacity</a>.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the rule group that helps with identification. </p>"""
    rules: NotRequired["capo_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    label_namespace: NotRequired["capo_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for your rule groups is the following: </p> <p> <code>awswaf:<account ID>:rulegroup:<rule group name>:</code> </p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""
    custom_response_bodies: NotRequired[
        "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    """<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""
    available_labels: NotRequired["capo_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the <code>RuleLabels</code> for a <a>Rule</a>.</p>"""
    consumed_labels: NotRequired["capo_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a <code>LabelMatchStatement</code> specification, in the <a>Statement</a> definition of a rule. </p>"""
    monetization_config: NotRequired[
        "capo_wafv2.types.monetization_config.MonetizationConfig"
    ]
    """<p>The monetization configuration for the rule group. Required when any rule in the rule group uses the <code>Monetize</code> action. When a rule group with a <code>MonetizationConfig</code> is used in a web ACL, the rule group's configuration applies to rules within that group unless overridden at the web ACL level.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Capacity"] = value["capacity"]
    out["ARN"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import capo_wafv2.types.rules

        out["Rules"] = capo_wafv2.types.rules.serialize_aws_json_1_1(value["rules"])
    import capo_wafv2.types.visibility_config

    out["VisibilityConfig"] = capo_wafv2.types.visibility_config.serialize_aws_json_1_1(
        value["visibility_config"]
    )
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    if "custom_response_bodies" in value:
        import capo_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            capo_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    if "available_labels" in value:
        import capo_wafv2.types.label_summaries

        out["AvailableLabels"] = (
            capo_wafv2.types.label_summaries.serialize_aws_json_1_1(
                value["available_labels"]
            )
        )
    if "consumed_labels" in value:
        import capo_wafv2.types.label_summaries

        out["ConsumedLabels"] = capo_wafv2.types.label_summaries.serialize_aws_json_1_1(
            value["consumed_labels"]
        )
    if "monetization_config" in value:
        import capo_wafv2.types.monetization_config

        out["MonetizationConfig"] = (
            capo_wafv2.types.monetization_config.serialize_aws_json_1_1(
                value["monetization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleGroup:
    out: RuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RuleGroup.name required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("RuleGroup.id required")
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("RuleGroup.capacity required")
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("RuleGroup.arn required")
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
        raise DeserializationError("RuleGroup.visibility_config required")
    if data.get("LabelNamespace") is not None:
        out["label_namespace"] = data["LabelNamespace"]
    if data.get("CustomResponseBodies") is not None:
        import capo_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            capo_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    if data.get("AvailableLabels") is not None:
        import capo_wafv2.types.label_summaries

        out["available_labels"] = (
            capo_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["AvailableLabels"]
            )
        )
    if data.get("ConsumedLabels") is not None:
        import capo_wafv2.types.label_summaries

        out["consumed_labels"] = (
            capo_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["ConsumedLabels"]
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
