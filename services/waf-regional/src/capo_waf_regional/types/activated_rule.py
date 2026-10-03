"""Generated from Smithy shape ``com.amazonaws.wafregional#ActivatedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.excluded_rules
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.rule_priority
    import capo_waf_regional.types.waf_action
    import capo_waf_regional.types.waf_override_action
    import capo_waf_regional.types.waf_rule_type


class ActivatedRule(TypedDict, closed=True):
    priority: "capo_waf_regional.types.rule_priority.RulePriority"
    """<p>Specifies the order in which the <code>Rules</code> in a <code>WebACL</code> are evaluated. Rules with a lower value for <code>Priority</code> are evaluated before <code>Rules</code> with a higher value. The value must be a unique integer. If you add multiple <code>Rules</code> to a <code>WebACL</code>, the values don't need to be consecutive.</p>"""
    rule_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> for a <code>Rule</code>. You use <code>RuleId</code> to get more information about a <code>Rule</code> (see <a>GetRule</a>), update a <code>Rule</code> (see <a>UpdateRule</a>), insert a <code>Rule</code> into a <code>WebACL</code> or delete a one from a <code>WebACL</code> (see <a>UpdateWebACL</a>), or delete a <code>Rule</code> from AWS WAF (see <a>DeleteRule</a>).</p> <p> <code>RuleId</code> is returned by <a>CreateRule</a> and by <a>ListRules</a>.</p>"""
    action: NotRequired["capo_waf_regional.types.waf_action.WafAction"]
    """<p>Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the <code>Rule</code>. Valid values for <code>Action</code> include the following:</p> <ul> <li> <p> <code>ALLOW</code>: CloudFront responds with the requested object.</p> </li> <li> <p> <code>BLOCK</code>: CloudFront responds with an HTTP 403 (Forbidden) status code.</p> </li> <li> <p> <code>COUNT</code>: AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL. </p> </li> </ul> <p> <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case, you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>.</p>"""
    override_action: NotRequired[
        "capo_waf_regional.types.waf_override_action.WafOverrideAction"
    ]
    """<p>Use the <code>OverrideAction</code> to test your <code>RuleGroup</code>.</p> <p>Any rule in a <code>RuleGroup</code> can potentially block a request. If you set the <code>OverrideAction</code> to <code>None</code>, the <code>RuleGroup</code> will block a request if any individual rule in the <code>RuleGroup</code> matches the request and is configured to block that request. However if you first want to test the <code>RuleGroup</code>, set the <code>OverrideAction</code> to <code>Count</code>. The <code>RuleGroup</code> will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using <a>GetSampledRequests</a>. </p> <p> <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>.</p>"""
    type: NotRequired["capo_waf_regional.types.waf_rule_type.WafRuleType"]
    """<p>The rule type, either <code>REGULAR</code>, as defined by <a>Rule</a>, <code>RATE_BASED</code>, as defined by <a>RateBasedRule</a>, or <code>GROUP</code>, as defined by <a>RuleGroup</a>. The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the <a>UpdateWebACL</a> request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. </p>"""
    excluded_rules: NotRequired["capo_waf_regional.types.excluded_rules.ExcludedRules"]
    """<p>An array of rules to exclude from a rule group. This is applicable only when the <code>ActivatedRule</code> refers to a <code>RuleGroup</code>.</p> <p>Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.</p> <p>Specifying <code>ExcludedRules</code> does not remove those rules from the rule group. Rather, it changes the action for the rules to <code>COUNT</code>. Therefore, requests that match an <code>ExcludedRule</code> are counted but not blocked. The <code>RuleGroup</code> owner will receive COUNT metrics for each <code>ExcludedRule</code>.</p> <p>If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:</p> <ol> <li> <p>Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging.html">Logging Web ACL Traffic Information</a>.</p> </li> <li> <p>Submit an <a>UpdateWebACL</a> request that has two actions:</p> <ul> <li> <p>The first action deletes the existing rule group from the web ACL. That is, in the <a>UpdateWebACL</a> request, the first <code>Updates:Action</code> should be <code>DELETE</code> and <code>Updates:ActivatedRule:RuleId</code> should be the rule group that contains the rules that you want to exclude.</p> </li> <li> <p>The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second <code>Updates:Action</code> should be <code>INSERT</code>, <code>Updates:ActivatedRule:RuleId</code> should be the rule group that you just removed, and <code>ExcludedRules</code> should contain the rules that you want to exclude.</p> </li> </ul> </li> </ol>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivatedRule) -> dict:
    out: dict = {}
    out["Priority"] = value["priority"]
    out["RuleId"] = value["rule_id"]
    if "action" in value:
        import capo_waf_regional.types.waf_action

        out["Action"] = capo_waf_regional.types.waf_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "override_action" in value:
        import capo_waf_regional.types.waf_override_action

        out["OverrideAction"] = (
            capo_waf_regional.types.waf_override_action.serialize_aws_json_1_1(
                value["override_action"]
            )
        )
    if "type" in value:
        import capo_waf_regional.types.waf_rule_type

        out["Type"] = capo_waf_regional.types.waf_rule_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "excluded_rules" in value:
        import capo_waf_regional.types.excluded_rules

        out["ExcludedRules"] = (
            capo_waf_regional.types.excluded_rules.serialize_aws_json_1_1(
                value["excluded_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivatedRule:
    out: ActivatedRule = {}  # type: ignore[typeddict-item]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("ActivatedRule.priority required")
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("ActivatedRule.rule_id required")
    if data.get("Action") is not None:
        import capo_waf_regional.types.waf_action

        out["action"] = capo_waf_regional.types.waf_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("OverrideAction") is not None:
        import capo_waf_regional.types.waf_override_action

        out["override_action"] = (
            capo_waf_regional.types.waf_override_action.deserialize_aws_json_1_1(
                data["OverrideAction"]
            )
        )
    if data.get("Type") is not None:
        import capo_waf_regional.types.waf_rule_type

        out["type"] = capo_waf_regional.types.waf_rule_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("ExcludedRules") is not None:
        import capo_waf_regional.types.excluded_rules

        out["excluded_rules"] = (
            capo_waf_regional.types.excluded_rules.deserialize_aws_json_1_1(
                data["ExcludedRules"]
            )
        )
    return out
