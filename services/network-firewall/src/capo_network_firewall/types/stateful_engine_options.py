"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulEngineOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_timeouts
    import capo_network_firewall.types.rule_order
    import capo_network_firewall.types.stream_exception_policy


class StatefulEngineOptions(TypedDict, closed=True):
    rule_order: NotRequired["capo_network_firewall.types.rule_order.RuleOrder"]
    """<p>Indicates how to manage the order of stateful rule evaluation for the policy. <code>STRICT_ORDER</code> is the recommended option, but <code>DEFAULT_ACTION_ORDER</code> is the default option. With <code>STRICT_ORDER</code>, provide your rules in the order that you want them to be evaluated. You can then choose one or more default actions for packets that don't match any rules. Choose <code>STRICT_ORDER</code> to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is <code>PASS</code>, followed by <code>DROP</code>, <code>REJECT</code>, and <code>ALERT</code> actions. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on your settings. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html">Evaluation order for stateful rules</a> in the <i>Network Firewall Developer Guide</i>. </p>"""
    stream_exception_policy: NotRequired[
        "capo_network_firewall.types.stream_exception_policy.StreamExceptionPolicy"
    ]
    """<p>Configures how Network Firewall processes traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself.</p> <ul> <li> <p> <code>DROP</code> - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.</p> </li> <li> <p> <code>CONTINUE</code> - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to <code>drop http</code> traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a <code>flow:stateless</code> rule would still match, as would the <code>aws:drop_strict</code> default action.</p> </li> <li> <p> <code>REJECT</code> - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.</p> </li> </ul>"""
    flow_timeouts: NotRequired["capo_network_firewall.types.flow_timeouts.FlowTimeouts"]
    """<p>Configures the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulEngineOptions) -> dict:
    out: dict = {}
    if "rule_order" in value:
        import capo_network_firewall.types.rule_order

        out["RuleOrder"] = (
            capo_network_firewall.types.rule_order.serialize_aws_json_1_0(
                value["rule_order"]
            )
        )
    if "stream_exception_policy" in value:
        import capo_network_firewall.types.stream_exception_policy

        out["StreamExceptionPolicy"] = (
            capo_network_firewall.types.stream_exception_policy.serialize_aws_json_1_0(
                value["stream_exception_policy"]
            )
        )
    if "flow_timeouts" in value:
        import capo_network_firewall.types.flow_timeouts

        out["FlowTimeouts"] = (
            capo_network_firewall.types.flow_timeouts.serialize_aws_json_1_0(
                value["flow_timeouts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulEngineOptions:
    out: StatefulEngineOptions = {}  # type: ignore[typeddict-item]
    if data.get("RuleOrder") is not None:
        import capo_network_firewall.types.rule_order

        out["rule_order"] = (
            capo_network_firewall.types.rule_order.deserialize_aws_json_1_0(
                data["RuleOrder"]
            )
        )
    if data.get("StreamExceptionPolicy") is not None:
        import capo_network_firewall.types.stream_exception_policy

        out["stream_exception_policy"] = (
            capo_network_firewall.types.stream_exception_policy.deserialize_aws_json_1_0(
                data["StreamExceptionPolicy"]
            )
        )
    if data.get("FlowTimeouts") is not None:
        import capo_network_firewall.types.flow_timeouts

        out["flow_timeouts"] = (
            capo_network_firewall.types.flow_timeouts.deserialize_aws_json_1_0(
                data["FlowTimeouts"]
            )
        )
    return out
