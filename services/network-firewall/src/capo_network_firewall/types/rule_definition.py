"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.match_attributes
    import capo_network_firewall.types.stateless_actions


class RuleDefinition(TypedDict, closed=True):
    match_attributes: "capo_network_firewall.types.match_attributes.MatchAttributes"
    """<p>Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags. </p>"""
    actions: "capo_network_firewall.types.stateless_actions.StatelessActions"
    """<p>The actions to take on a packet that matches one of the stateless rule definition's match attributes. You must specify a standard action and you can add custom actions. </p> <note> <p>Network Firewall only forwards a packet for stateful rule inspection if you specify <code>aws:forward_to_sfe</code> for a rule that the packet matches, or if the packet doesn't match any stateless rule and you specify <code>aws:forward_to_sfe</code> for the <code>StatelessDefaultActions</code> setting for the <a>FirewallPolicy</a>.</p> </note> <p>For every rule, you must specify exactly one of the following standard actions. </p> <ul> <li> <p> <b>aws:pass</b> - Discontinues all inspection of the packet and permits it to go to its intended destination.</p> </li> <li> <p> <b>aws:drop</b> - Discontinues all inspection of the packet and blocks it from going to its intended destination.</p> </li> <li> <p> <b>aws:forward_to_sfe</b> - Discontinues stateless inspection of the packet and forwards it to the stateful rule engine for inspection. </p> </li> </ul> <p>Additionally, you can specify a custom action. To do this, you define a custom action by name and type, then provide the name you've assigned to the action in this <code>Actions</code> setting. For information about the options, see <a>CustomAction</a>. </p> <p>To provide more than one action in this setting, separate the settings with a comma. For example, if you have a custom <code>PublishMetrics</code> action that you've named <code>MyMetricsAction</code>, then you could specify the standard action <code>aws:pass</code> and the custom action with <code>[“aws:pass”, “MyMetricsAction”]</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDefinition) -> dict:
    out: dict = {}
    import capo_network_firewall.types.match_attributes

    out["MatchAttributes"] = (
        capo_network_firewall.types.match_attributes.serialize_aws_json_1_0(
            value["match_attributes"]
        )
    )
    import capo_network_firewall.types.stateless_actions

    out["Actions"] = (
        capo_network_firewall.types.stateless_actions.serialize_aws_json_1_0(
            value["actions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleDefinition:
    out: RuleDefinition = {}  # type: ignore[typeddict-item]
    if data.get("MatchAttributes") is not None:
        import capo_network_firewall.types.match_attributes

        out["match_attributes"] = (
            capo_network_firewall.types.match_attributes.deserialize_aws_json_1_0(
                data["MatchAttributes"]
            )
        )
    else:
        raise DeserializationError("RuleDefinition.match_attributes required")
    if data.get("Actions") is not None:
        import capo_network_firewall.types.stateless_actions

        out["actions"] = (
            capo_network_firewall.types.stateless_actions.deserialize_aws_json_1_0(
                data["Actions"]
            )
        )
    else:
        out["actions"] = []
    return out
