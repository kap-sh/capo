"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RulesSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.rules_source_list
    import capo_network_firewall.types.rules_string
    import capo_network_firewall.types.stateful_rules
    import capo_network_firewall.types.stateless_rules_and_custom_actions


class RulesSource(TypedDict, closed=True):
    rules_string: NotRequired["capo_network_firewall.types.rules_string.RulesString"]
    """<p>Stateful inspection criteria, provided in Suricata compatible rules. Suricata is an open-source threat detection framework that includes a standard rule-based language for network traffic inspection.</p> <p>These rules contain the inspection criteria and the action to take for traffic that matches the criteria, so this type of rule group doesn't have a separate action setting.</p> <note> <p>You can't use the <code>priority</code> keyword if the <code>RuleOrder</code> option in <a>StatefulRuleOptions</a> is set to <code>STRICT_ORDER</code>.</p> </note>"""
    rules_source_list: NotRequired[
        "capo_network_firewall.types.rules_source_list.RulesSourceList"
    ]
    """<p>Stateful inspection criteria for a domain list rule group. </p>"""
    stateful_rules: NotRequired[
        "capo_network_firewall.types.stateful_rules.StatefulRules"
    ]
    """<p>An array of individual stateful rules inspection criteria to be used together in a stateful rule group. Use this option to specify simple Suricata rules with protocol, source and destination, ports, direction, and rule options. For information about the Suricata <code>Rules</code> format, see <a href="https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html">Rules Format</a>. </p>"""
    stateless_rules_and_custom_actions: NotRequired[
        "capo_network_firewall.types.stateless_rules_and_custom_actions.StatelessRulesAndCustomActions"
    ]
    """<p>Stateless inspection criteria to be used in a stateless rule group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RulesSource) -> dict:
    out: dict = {}
    if "rules_string" in value:
        out["RulesString"] = value["rules_string"]
    if "rules_source_list" in value:
        import capo_network_firewall.types.rules_source_list

        out["RulesSourceList"] = (
            capo_network_firewall.types.rules_source_list.serialize_aws_json_1_0(
                value["rules_source_list"]
            )
        )
    if "stateful_rules" in value:
        import capo_network_firewall.types.stateful_rules

        out["StatefulRules"] = (
            capo_network_firewall.types.stateful_rules.serialize_aws_json_1_0(
                value["stateful_rules"]
            )
        )
    if "stateless_rules_and_custom_actions" in value:
        import capo_network_firewall.types.stateless_rules_and_custom_actions

        out["StatelessRulesAndCustomActions"] = (
            capo_network_firewall.types.stateless_rules_and_custom_actions.serialize_aws_json_1_0(
                value["stateless_rules_and_custom_actions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RulesSource:
    out: RulesSource = {}  # type: ignore[typeddict-item]
    if data.get("RulesString") is not None:
        out["rules_string"] = data["RulesString"]
    if data.get("RulesSourceList") is not None:
        import capo_network_firewall.types.rules_source_list

        out["rules_source_list"] = (
            capo_network_firewall.types.rules_source_list.deserialize_aws_json_1_0(
                data["RulesSourceList"]
            )
        )
    if data.get("StatefulRules") is not None:
        import capo_network_firewall.types.stateful_rules

        out["stateful_rules"] = (
            capo_network_firewall.types.stateful_rules.deserialize_aws_json_1_0(
                data["StatefulRules"]
            )
        )
    if data.get("StatelessRulesAndCustomActions") is not None:
        import capo_network_firewall.types.stateless_rules_and_custom_actions

        out["stateless_rules_and_custom_actions"] = (
            capo_network_firewall.types.stateless_rules_and_custom_actions.deserialize_aws_json_1_0(
                data["StatelessRulesAndCustomActions"]
            )
        )
    return out
