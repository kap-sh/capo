"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.reference_sets
    import capo_network_firewall.types.rule_variables
    import capo_network_firewall.types.rules_source
    import capo_network_firewall.types.stateful_rule_options


class RuleGroup(TypedDict, closed=True):
    rule_variables: NotRequired[
        "capo_network_firewall.types.rule_variables.RuleVariables"
    ]
    """<p>Settings that are available for use in the rules in the rule group. You can only use these for stateful rule groups. </p>"""
    reference_sets: NotRequired[
        "capo_network_firewall.types.reference_sets.ReferenceSets"
    ]
    """<p>The list of a rule group's reference sets.</p>"""
    rules_source: "capo_network_firewall.types.rules_source.RulesSource"
    """<p>The stateful rules or stateless rules for the rule group. </p>"""
    stateful_rule_options: NotRequired[
        "capo_network_firewall.types.stateful_rule_options.StatefulRuleOptions"
    ]
    """<p>Additional options governing how Network Firewall handles stateful rules. The policies where you use your stateful rule group must have stateful rule options settings that are compatible with these settings. Some limitations apply; for more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html">Strict evaluation order</a> in the <i>Network Firewall Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroup) -> dict:
    out: dict = {}
    if "rule_variables" in value:
        import capo_network_firewall.types.rule_variables

        out["RuleVariables"] = (
            capo_network_firewall.types.rule_variables.serialize_aws_json_1_0(
                value["rule_variables"]
            )
        )
    if "reference_sets" in value:
        import capo_network_firewall.types.reference_sets

        out["ReferenceSets"] = (
            capo_network_firewall.types.reference_sets.serialize_aws_json_1_0(
                value["reference_sets"]
            )
        )
    import capo_network_firewall.types.rules_source

    out["RulesSource"] = (
        capo_network_firewall.types.rules_source.serialize_aws_json_1_0(
            value["rules_source"]
        )
    )
    if "stateful_rule_options" in value:
        import capo_network_firewall.types.stateful_rule_options

        out["StatefulRuleOptions"] = (
            capo_network_firewall.types.stateful_rule_options.serialize_aws_json_1_0(
                value["stateful_rule_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleGroup:
    out: RuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RuleVariables") is not None:
        import capo_network_firewall.types.rule_variables

        out["rule_variables"] = (
            capo_network_firewall.types.rule_variables.deserialize_aws_json_1_0(
                data["RuleVariables"]
            )
        )
    if data.get("ReferenceSets") is not None:
        import capo_network_firewall.types.reference_sets

        out["reference_sets"] = (
            capo_network_firewall.types.reference_sets.deserialize_aws_json_1_0(
                data["ReferenceSets"]
            )
        )
    if data.get("RulesSource") is not None:
        import capo_network_firewall.types.rules_source

        out["rules_source"] = (
            capo_network_firewall.types.rules_source.deserialize_aws_json_1_0(
                data["RulesSource"]
            )
        )
    else:
        raise DeserializationError("RuleGroup.rules_source required")
    if data.get("StatefulRuleOptions") is not None:
        import capo_network_firewall.types.stateful_rule_options

        out["stateful_rule_options"] = (
            capo_network_firewall.types.stateful_rule_options.deserialize_aws_json_1_0(
                data["StatefulRuleOptions"]
            )
        )
    return out
