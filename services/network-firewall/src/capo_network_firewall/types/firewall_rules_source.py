"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRulesSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_rules
    import capo_network_firewall.types.rules_source_list
    import capo_network_firewall.types.rules_string


class FirewallRulesSource(TypedDict, closed=True):
    rules_string: NotRequired["capo_network_firewall.types.rules_string.RulesString"]
    """<p>Firewall engine rules, provided as a single Suricata-compatible rule string in firewall mode. Use this to provide rules that you've already written in the Suricata firewall-mode format. For the rule format, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html">Rule groups for a firewall using a Next Generation policy</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    firewall_rules: NotRequired[
        "capo_network_firewall.types.firewall_rules.FirewallRules"
    ]
    """<p>An array of individual firewall engine rules, provided as structured rules rather than as a rule string.</p>"""
    rules_source_list: NotRequired[
        "capo_network_firewall.types.rules_source_list.RulesSourceList"
    ]
    """<p>Stateful inspection criteria for a domain list, specified as the list of domain names that Network Firewall generates firewall engine rules from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRulesSource) -> dict:
    out: dict = {}
    if "rules_string" in value:
        out["RulesString"] = value["rules_string"]
    if "firewall_rules" in value:
        import capo_network_firewall.types.firewall_rules

        out["FirewallRules"] = (
            capo_network_firewall.types.firewall_rules.serialize_aws_json_1_0(
                value["firewall_rules"]
            )
        )
    if "rules_source_list" in value:
        import capo_network_firewall.types.rules_source_list

        out["RulesSourceList"] = (
            capo_network_firewall.types.rules_source_list.serialize_aws_json_1_0(
                value["rules_source_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallRulesSource:
    out: FirewallRulesSource = {}  # type: ignore[typeddict-item]
    if data.get("RulesString") is not None:
        out["rules_string"] = data["RulesString"]
    if data.get("FirewallRules") is not None:
        import capo_network_firewall.types.firewall_rules

        out["firewall_rules"] = (
            capo_network_firewall.types.firewall_rules.deserialize_aws_json_1_0(
                data["FirewallRules"]
            )
        )
    if data.get("RulesSourceList") is not None:
        import capo_network_firewall.types.rules_source_list

        out["rules_source_list"] = (
            capo_network_firewall.types.rules_source_list.deserialize_aws_json_1_0(
                data["RulesSourceList"]
            )
        )
    return out
