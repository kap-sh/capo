"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleGroupReferenceStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.excluded_rules
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.rule_action_overrides


class RuleGroupReferenceStatement(TypedDict, closed=True):
    arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    excluded_rules: NotRequired["capo_wafv2.types.excluded_rules.ExcludedRules"]
    """<p>Rules in the referenced rule group whose actions are set to <code>Count</code>. </p> <note> <p>Instead of this option, use <code>RuleActionOverrides</code>. It accepts any valid action setting, including <code>Count</code>.</p> </note>"""
    rule_action_overrides: NotRequired[
        "capo_wafv2.types.rule_action_overrides.RuleActionOverrides"
    ]
    """<p>Action settings to use in the place of the rule actions that are configured inside the rule group. You specify one override for each rule whose action you want to change. </p> <note> <p>Verify the rule names in your overrides carefully. With managed rule groups, WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.</p> </note> <p>You can use overrides for testing, for example you can override all of rule actions to <code>Count</code> and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroupReferenceStatement) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    if "excluded_rules" in value:
        import capo_wafv2.types.excluded_rules

        out["ExcludedRules"] = capo_wafv2.types.excluded_rules.serialize_aws_json_1_1(
            value["excluded_rules"]
        )
    if "rule_action_overrides" in value:
        import capo_wafv2.types.rule_action_overrides

        out["RuleActionOverrides"] = (
            capo_wafv2.types.rule_action_overrides.serialize_aws_json_1_1(
                value["rule_action_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleGroupReferenceStatement:
    out: RuleGroupReferenceStatement = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    if data.get("ExcludedRules") is not None:
        import capo_wafv2.types.excluded_rules

        out["excluded_rules"] = (
            capo_wafv2.types.excluded_rules.deserialize_aws_json_1_1(
                data["ExcludedRules"]
            )
        )
    if data.get("RuleActionOverrides") is not None:
        import capo_wafv2.types.rule_action_overrides

        out["rule_action_overrides"] = (
            capo_wafv2.types.rule_action_overrides.deserialize_aws_json_1_1(
                data["RuleActionOverrides"]
            )
        )
    return out
