"""Generated from Smithy shape ``com.amazonaws.wafv2#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.captcha_config
    import capo_wafv2.types.challenge_config
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.labels
    import capo_wafv2.types.override_action
    import capo_wafv2.types.rule_action
    import capo_wafv2.types.rule_priority
    import capo_wafv2.types.statement
    import capo_wafv2.types.visibility_config


class Rule(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule. </p> <p>If you change the name of a <code>Rule</code> after you create it and you want the rule's metric name to reflect the change, update the metric name in the rule's <code>VisibilityConfig</code> settings. WAF doesn't automatically update the metric name when you update the rule name. </p>"""
    priority: "capo_wafv2.types.rule_priority.RulePriority"
    """<p>If you define more than one <code>Rule</code> in a <code>WebACL</code>, WAF evaluates each request against the <code>Rules</code> in order based on the value of <code>Priority</code>. WAF processes rules with lower priority first. The priorities don't need to be consecutive, but they must all be different.</p>"""
    statement: "capo_wafv2.types.statement.Statement"
    """<p>The WAF processing statement for the rule, for example <a>ByteMatchStatement</a> or <a>SizeConstraintStatement</a>. </p>"""
    action: NotRequired["capo_wafv2.types.rule_action.RuleAction"]
    """<p>The action that WAF should take on a web request when it matches the rule statement. Settings at the web ACL level can override the rule action setting. </p> <p>This is used only for rules whose statements do not reference a rule group. Rule statements that reference a rule group include <code>RuleGroupReferenceStatement</code> and <code>ManagedRuleGroupStatement</code>. </p> <p>You must specify either this <code>Action</code> setting or the rule <code>OverrideAction</code> setting, but not both:</p> <ul> <li> <p>If the rule statement does not reference a rule group, use this rule action setting and not the rule override action setting. </p> </li> <li> <p>If the rule statement references a rule group, use the override action setting and not this action setting. </p> </li> </ul>"""
    override_action: NotRequired["capo_wafv2.types.override_action.OverrideAction"]
    """<p>The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only. </p> <p>You can only use this for rule statements that reference a rule group, like <code>RuleGroupReferenceStatement</code> and <code>ManagedRuleGroupStatement</code>. </p> <note> <p>This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with <code>Count</code> action, in your rule group reference statement settings. </p> </note>"""
    rule_labels: NotRequired["capo_wafv2.types.labels.Labels"]
    """<p>Labels to apply to web requests that match the rule match statement. WAF applies fully qualified labels to matching web requests. A fully qualified label is the concatenation of a label namespace and a rule label. The rule's rule group or web ACL defines the label namespace. </p> <note> <p>Any rule that isn't a rule group reference statement or managed rule group statement can add labels to matching web requests.</p> </note> <p>Rules that run after this rule in the web ACL can match against these labels using a <code>LabelMatchStatement</code>.</p> <p>For each label, provide a case-sensitive string containing optional namespaces and a label name, according to the following guidelines:</p> <ul> <li> <p>Separate each component of the label with a colon. </p> </li> <li> <p>Each namespace or name can have up to 128 characters.</p> </li> <li> <p>You can specify up to 5 namespaces in a label.</p> </li> <li> <p>Don't use the following reserved words in your label specification: <code>aws</code>, <code>waf</code>, <code>managed</code>, <code>rulegroup</code>, <code>webacl</code>, <code>regexpatternset</code>, or <code>ipset</code>.</p> </li> </ul> <p>For example, <code>myLabelName</code> or <code>nameSpace1:nameSpace2:myLabelName</code>. </p>"""
    visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p> <p>If you change the name of a <code>Rule</code> after you create it and you want the rule's metric name to reflect the change, update the metric name as well. WAF doesn't automatically update the metric name. </p>"""
    captcha_config: NotRequired["capo_wafv2.types.captcha_config.CaptchaConfig"]
    """<p>Specifies how WAF should handle <code>CAPTCHA</code> evaluations. If you don't specify this, WAF uses the <code>CAPTCHA</code> configuration that's defined for the web ACL. </p>"""
    challenge_config: NotRequired["capo_wafv2.types.challenge_config.ChallengeConfig"]
    """<p>Specifies how WAF should handle <code>Challenge</code> evaluations. If you don't specify this, WAF uses the challenge configuration that's defined for the web ACL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Priority"] = value.get("priority", 0)
    import capo_wafv2.types.statement

    out["Statement"] = capo_wafv2.types.statement.serialize_aws_json_1_1(
        value["statement"]
    )
    if "action" in value:
        import capo_wafv2.types.rule_action

        out["Action"] = capo_wafv2.types.rule_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "override_action" in value:
        import capo_wafv2.types.override_action

        out["OverrideAction"] = capo_wafv2.types.override_action.serialize_aws_json_1_1(
            value["override_action"]
        )
    if "rule_labels" in value:
        import capo_wafv2.types.labels

        out["RuleLabels"] = capo_wafv2.types.labels.serialize_aws_json_1_1(
            value["rule_labels"]
        )
    import capo_wafv2.types.visibility_config

    out["VisibilityConfig"] = capo_wafv2.types.visibility_config.serialize_aws_json_1_1(
        value["visibility_config"]
    )
    if "captcha_config" in value:
        import capo_wafv2.types.captcha_config

        out["CaptchaConfig"] = capo_wafv2.types.captcha_config.serialize_aws_json_1_1(
            value["captcha_config"]
        )
    if "challenge_config" in value:
        import capo_wafv2.types.challenge_config

        out["ChallengeConfig"] = (
            capo_wafv2.types.challenge_config.serialize_aws_json_1_1(
                value["challenge_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("Statement") is not None:
        import capo_wafv2.types.statement

        out["statement"] = capo_wafv2.types.statement.deserialize_aws_json_1_1(
            data["Statement"]
        )
    else:
        raise DeserializationError("Rule.statement required")
    if data.get("Action") is not None:
        import capo_wafv2.types.rule_action

        out["action"] = capo_wafv2.types.rule_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("OverrideAction") is not None:
        import capo_wafv2.types.override_action

        out["override_action"] = (
            capo_wafv2.types.override_action.deserialize_aws_json_1_1(
                data["OverrideAction"]
            )
        )
    if data.get("RuleLabels") is not None:
        import capo_wafv2.types.labels

        out["rule_labels"] = capo_wafv2.types.labels.deserialize_aws_json_1_1(
            data["RuleLabels"]
        )
    if data.get("VisibilityConfig") is not None:
        import capo_wafv2.types.visibility_config

        out["visibility_config"] = (
            capo_wafv2.types.visibility_config.deserialize_aws_json_1_1(
                data["VisibilityConfig"]
            )
        )
    else:
        raise DeserializationError("Rule.visibility_config required")
    if data.get("CaptchaConfig") is not None:
        import capo_wafv2.types.captcha_config

        out["captcha_config"] = (
            capo_wafv2.types.captcha_config.deserialize_aws_json_1_1(
                data["CaptchaConfig"]
            )
        )
    if data.get("ChallengeConfig") is not None:
        import capo_wafv2.types.challenge_config

        out["challenge_config"] = (
            capo_wafv2.types.challenge_config.deserialize_aws_json_1_1(
                data["ChallengeConfig"]
            )
        )
    return out
