"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.excluded_rules
    import capo_wafv2.types.managed_rule_group_configs
    import capo_wafv2.types.rule_action_overrides
    import capo_wafv2.types.statement
    import capo_wafv2.types.vendor_name
    import capo_wafv2.types.version_key_string


class ManagedRuleGroupStatement(TypedDict, closed=True):
    vendor_name: "capo_wafv2.types.vendor_name.VendorName"
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>"""
    version: NotRequired["capo_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The version of the managed rule group to use. If you specify this, the version setting is fixed until you change it. If you don't specify this, WAF uses the vendor's default version, and then keeps the version at the vendor's default when the vendor updates the managed rule group settings. </p>"""
    excluded_rules: NotRequired["capo_wafv2.types.excluded_rules.ExcludedRules"]
    """<p>Rules in the referenced rule group whose actions are set to <code>Count</code>. </p> <note> <p>Instead of this option, use <code>RuleActionOverrides</code>. It accepts any valid action setting, including <code>Count</code>.</p> </note>"""
    scope_down_statement: NotRequired["capo_wafv2.types.statement.Statement"]
    """<p>An optional nested statement that narrows the scope of the web requests that are evaluated by the managed rule group. Requests are only evaluated by the rule group if they match the scope-down statement. You can use any nestable <a>Statement</a> in the scope-down statement, and you can nest statements at any level, the same as you can for a rule statement. </p>"""
    managed_rule_group_configs: NotRequired[
        "capo_wafv2.types.managed_rule_group_configs.ManagedRuleGroupConfigs"
    ]
    """<p>Additional information that's used by a managed rule group. Many managed rule groups don't require this.</p> <p>The rule groups used for intelligent threat mitigation require additional configuration: </p> <ul> <li> <p>Use the <code>AWSManagedRulesACFPRuleSet</code> configuration object to configure the account creation fraud prevention managed rule group. The configuration includes the registration and sign-up pages of your application and the locations in the account creation request payload of data, such as the user email and phone number fields. </p> </li> <li> <p>Use the <code>AWSManagedRulesAntiDDoSRuleSet</code> configuration object to configure the anti-DDoS managed rule group. The configuration includes the sensitivity levels to use in the rules that typically block and challenge requests that might be participating in DDoS attacks and the specification to use to indicate whether a request can handle a silent browser challenge. </p> </li> <li> <p>Use the <code>AWSManagedRulesATPRuleSet</code> configuration object to configure the account takeover prevention managed rule group. The configuration includes the sign-in page of your application and the locations in the login request payload of data such as the username and password. </p> </li> <li> <p>Use the <code>AWSManagedRulesBotControlRuleSet</code> configuration object to configure the protection level that you want the Bot Control rule group to use. </p> </li> </ul>"""
    rule_action_overrides: NotRequired[
        "capo_wafv2.types.rule_action_overrides.RuleActionOverrides"
    ]
    """<p>Action settings to use in the place of the rule actions that are configured inside the rule group. You specify one override for each rule whose action you want to change. </p> <note> <p>Verify the rule names in your overrides carefully. With managed rule groups, WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.</p> </note> <p>You can use overrides for testing, for example you can override all of rule actions to <code>Count</code> and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupStatement) -> dict:
    out: dict = {}
    out["VendorName"] = value["vendor_name"]
    out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "excluded_rules" in value:
        import capo_wafv2.types.excluded_rules

        out["ExcludedRules"] = capo_wafv2.types.excluded_rules.serialize_aws_json_1_1(
            value["excluded_rules"]
        )
    if "scope_down_statement" in value:
        import capo_wafv2.types.statement

        out["ScopeDownStatement"] = capo_wafv2.types.statement.serialize_aws_json_1_1(
            value["scope_down_statement"]
        )
    if "managed_rule_group_configs" in value:
        import capo_wafv2.types.managed_rule_group_configs

        out["ManagedRuleGroupConfigs"] = (
            capo_wafv2.types.managed_rule_group_configs.serialize_aws_json_1_1(
                value["managed_rule_group_configs"]
            )
        )
    if "rule_action_overrides" in value:
        import capo_wafv2.types.rule_action_overrides

        out["RuleActionOverrides"] = (
            capo_wafv2.types.rule_action_overrides.serialize_aws_json_1_1(
                value["rule_action_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleGroupStatement:
    out: ManagedRuleGroupStatement = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    else:
        out["vendor_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("ExcludedRules") is not None:
        import capo_wafv2.types.excluded_rules

        out["excluded_rules"] = (
            capo_wafv2.types.excluded_rules.deserialize_aws_json_1_1(
                data["ExcludedRules"]
            )
        )
    if data.get("ScopeDownStatement") is not None:
        import capo_wafv2.types.statement

        out["scope_down_statement"] = (
            capo_wafv2.types.statement.deserialize_aws_json_1_1(
                data["ScopeDownStatement"]
            )
        )
    if data.get("ManagedRuleGroupConfigs") is not None:
        import capo_wafv2.types.managed_rule_group_configs

        out["managed_rule_group_configs"] = (
            capo_wafv2.types.managed_rule_group_configs.deserialize_aws_json_1_1(
                data["ManagedRuleGroupConfigs"]
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
