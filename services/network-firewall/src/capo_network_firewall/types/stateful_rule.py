"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.header
    import capo_network_firewall.types.rule_options
    import capo_network_firewall.types.stateful_action


class StatefulRule(TypedDict, closed=True):
    action: "capo_network_firewall.types.stateful_action.StatefulAction"
    """<p>Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow. </p> <p>The actions for a stateful rule are defined as follows: </p> <ul> <li> <p> <b>PASS</b> - Permits the packets to go to the intended destination.</p> </li> <li> <p> <b>DROP</b> - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the <a>Firewall</a> <a>LoggingConfiguration</a>. </p> </li> <li> <p> <b>ALERT</b> - Sends an alert log message, if alert logging is configured in the <a>Firewall</a> <a>LoggingConfiguration</a>. </p> <p>You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with <code>ALERT</code> action, verify in the logs that the rule is filtering as you want, then change the action to <code>DROP</code>.</p> </li> <li> <p> <b>REJECT</b> - Drops traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and an RST bit contained in the TCP header flags. REJECT is available only for TCP traffic. This option doesn't support FTP or IMAP protocols.</p> </li> </ul>"""
    header: "capo_network_firewall.types.header.Header"
    """<p>The stateful inspection criteria for this rule, used to inspect traffic flows. </p>"""
    rule_options: "capo_network_firewall.types.rule_options.RuleOptions"
    """<p>Additional options for the rule. These are the Suricata <code>RuleOptions</code> settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRule) -> dict:
    out: dict = {}
    import capo_network_firewall.types.stateful_action

    out["Action"] = capo_network_firewall.types.stateful_action.serialize_aws_json_1_0(
        value["action"]
    )
    import capo_network_firewall.types.header

    out["Header"] = capo_network_firewall.types.header.serialize_aws_json_1_0(
        value["header"]
    )
    import capo_network_firewall.types.rule_options

    out["RuleOptions"] = (
        capo_network_firewall.types.rule_options.serialize_aws_json_1_0(
            value["rule_options"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRule:
    out: StatefulRule = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_network_firewall.types.stateful_action

        out["action"] = (
            capo_network_firewall.types.stateful_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_network_firewall.types.stateful_action.StatefulAction", ""
        )
    if data.get("Header") is not None:
        import capo_network_firewall.types.header

        out["header"] = capo_network_firewall.types.header.deserialize_aws_json_1_0(
            data["Header"]
        )
    else:
        raise DeserializationError("StatefulRule.header required")
    if data.get("RuleOptions") is not None:
        import capo_network_firewall.types.rule_options

        out["rule_options"] = (
            capo_network_firewall.types.rule_options.deserialize_aws_json_1_0(
                data["RuleOptions"]
            )
        )
    else:
        out["rule_options"] = []
    return out
