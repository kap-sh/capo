"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.accept_prior_hooks
    import capo_network_firewall.types.action_scope
    import capo_network_firewall.types.alert_enabled
    import capo_network_firewall.types.bypass_ips_enabled
    import capo_network_firewall.types.destination
    import capo_network_firewall.types.firewall_rule_action
    import capo_network_firewall.types.firewall_rule_protocol
    import capo_network_firewall.types.hook_key
    import capo_network_firewall.types.port
    import capo_network_firewall.types.rule_metadata
    import capo_network_firewall.types.rule_options
    import capo_network_firewall.types.source


class FirewallRule(TypedDict, closed=True):
    action: "capo_network_firewall.types.firewall_rule_action.FirewallRuleAction"
    """<p>The action that the firewall engine takes on traffic that matches the rule. The firewall engine supports the following actions:</p> <ul> <li> <p> <code>ACCEPT</code> - Allow the traffic.</p> </li> <li> <p> <code>DROP</code> - Block the traffic and discontinue inspection.</p> </li> <li> <p> <code>REJECT</code> - Block the traffic and send a TCP reset packet back to the client.</p> </li> <li> <p> <code>REJECT_DST</code> - Block the traffic and send a TCP reset packet to the destination.</p> </li> <li> <p> <code>REJECT_BOTH</code> - Block the traffic and send a TCP reset packet to both the client and the destination.</p> </li> </ul> <p>You combine the action with an action scope, for example <code>accept:flow</code>. To send accepted traffic straight to its destination and skip the IPS engine, pair an accept action with the <code>BypassIPSEnabled</code> setting. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html">Rule groups for a firewall using a Next Generation policy</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    action_scope: "capo_network_firewall.types.action_scope.ActionScope"
    """<p>The scope that controls how much of the matched traffic the action applies to. The valid scopes depend on the action: <code>ACCEPT</code> supports all four scopes, and <code>DROP</code>, <code>REJECT</code>, <code>REJECT_DST</code>, and <code>REJECT_BOTH</code> support only <code>PACKET</code> and <code>FLOW</code>.</p> <ul> <li> <p> <code>PACKET</code> - The current packet only.</p> </li> <li> <p> <code>HOOK</code> - The current hook only. The firewall engine evaluates the connection again at the next hook.</p> </li> <li> <p> <code>TX</code> - The current transaction. The firewall engine continues to evaluate later transactions on the connection.</p> </li> <li> <p> <code>FLOW</code> - The entire connection. For an accept action, the connection skips the firewall engine's remaining hooks and advances to the IPS engine.</p> </li> </ul> <p>In a Suricata-compatible rule string, you write the scope in lowercase, for example <code>accept:flow</code>.</p>"""
    hook: "capo_network_firewall.types.hook_key.HookKey"
    """<p>The connection-state hook at which the firewall engine evaluates the rule. The hook encodes both the protocol and the connection state, for example a TCP hook or a TLS <code>client_hello</code> hook. For the hooks that the firewall engine supports and how they map to the connection lifecycle, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html">Rule groups for a firewall using a Next Generation policy</a> in the <i>Network Firewall Developer Guide</i> and the <a href="https://suricata.readthedocs.io/en/suricata-8.0.3/firewall/firewall-design.html">Suricata firewall mode documentation</a>.</p>"""
    protocol: "capo_network_firewall.types.firewall_rule_protocol.FirewallRuleProtocol"
    """<p>The protocol of the rule's hook. The protocol is derived from the hook and must match the hook's protocol prefix. Network Firewall rejects a rule whose protocol doesn't match its hook.</p>"""
    source_i_ps: NotRequired["capo_network_firewall.types.source.Source"]
    """<p>The source IP addresses and address ranges to inspect for, in CIDR notation. A firewall rule always compiles to a forward-direction rule, so you express inbound compared to outbound traffic through the source and destination addresses.</p>"""
    dest_i_ps: NotRequired["capo_network_firewall.types.destination.Destination"]
    """<p>The destination IP addresses and address ranges to inspect for, in CIDR notation. A firewall rule always compiles to a forward-direction rule, so you express inbound compared to outbound traffic through the source and destination addresses.</p>"""
    source_ports: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The source ports to inspect for.</p>"""
    dest_ports: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The destination ports to inspect for.</p>"""
    rule_options: NotRequired["capo_network_firewall.types.rule_options.RuleOptions"]
    """<p>Additional options for the rule. These are the Suricata <code>RuleOptions</code> settings, such as the signature ID (<code>sid</code>) and match keywords.</p>"""
    accept_prior_hooks: NotRequired[
        "capo_network_firewall.types.accept_prior_hooks.AcceptPriorHooks"
    ]
    """<p>Whether Network Firewall automatically accepts the earlier application-layer hooks that a connection must pass to reach this rule's hook. Because the firewall engine is drop by default, accepting prior hooks lets you author a single rule for the hook you care about, instead of also authoring a rule for each earlier hook. This setting accepts the earlier application-layer hooks only; it doesn't accept the TCP layer. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html">Rule groups for a firewall using a Next Generation policy</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    alert_enabled: NotRequired["capo_network_firewall.types.alert_enabled.AlertEnabled"]
    """<p>Specifies whether the rule also generates an alert log for the traffic that it matches. Turning on alerting adds a secondary alert action to the rule, so that Network Firewall logs the match in addition to taking the rule's primary action.</p>"""
    bypass_ips_enabled: NotRequired[
        "capo_network_firewall.types.bypass_ips_enabled.BypassIPSEnabled"
    ]
    """<p>Specifies whether an accepted connection bypasses the IPS engine. By default, traffic that the firewall engine accepts advances to the IPS engine for threat inspection. When you turn on this setting for an accept rule, the accepted traffic goes straight to its destination without IPS inspection. You can set the bypass only on accept rules, and it uses the same scope as the rule's accept action; only the <code>flow</code> and <code>packet</code> scopes support a bypass. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html">Rule groups for a firewall using a Next Generation policy</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    rule_metadata: NotRequired["capo_network_firewall.types.rule_metadata.RuleMetadata"]
    """<p>Optional metadata for the rule: whether the rule is enabled and a description. Metadata doesn't change how the rule matches or acts on traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRule) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_rule_action

    out["Action"] = (
        capo_network_firewall.types.firewall_rule_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    import capo_network_firewall.types.action_scope

    out["ActionScope"] = (
        capo_network_firewall.types.action_scope.serialize_aws_json_1_0(
            value["action_scope"]
        )
    )
    import capo_network_firewall.types.hook_key

    out["Hook"] = capo_network_firewall.types.hook_key.serialize_aws_json_1_0(
        value["hook"]
    )
    import capo_network_firewall.types.firewall_rule_protocol

    out["Protocol"] = (
        capo_network_firewall.types.firewall_rule_protocol.serialize_aws_json_1_0(
            value["protocol"]
        )
    )
    if "source_i_ps" in value:
        out["SourceIPs"] = value["source_i_ps"]
    if "dest_i_ps" in value:
        out["DestIPs"] = value["dest_i_ps"]
    if "source_ports" in value:
        out["SourcePorts"] = value["source_ports"]
    if "dest_ports" in value:
        out["DestPorts"] = value["dest_ports"]
    if "rule_options" in value:
        import capo_network_firewall.types.rule_options

        out["RuleOptions"] = (
            capo_network_firewall.types.rule_options.serialize_aws_json_1_0(
                value["rule_options"]
            )
        )
    if "accept_prior_hooks" in value:
        out["AcceptPriorHooks"] = value["accept_prior_hooks"]
    if "alert_enabled" in value:
        out["AlertEnabled"] = value["alert_enabled"]
    if "bypass_ips_enabled" in value:
        out["BypassIPSEnabled"] = value["bypass_ips_enabled"]
    if "rule_metadata" in value:
        import capo_network_firewall.types.rule_metadata

        out["RuleMetadata"] = (
            capo_network_firewall.types.rule_metadata.serialize_aws_json_1_0(
                value["rule_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallRule:
    out: FirewallRule = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_network_firewall.types.firewall_rule_action

        out["action"] = (
            capo_network_firewall.types.firewall_rule_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_network_firewall.types.firewall_rule_action.FirewallRuleAction", ""
        )
    if data.get("ActionScope") is not None:
        import capo_network_firewall.types.action_scope

        out["action_scope"] = (
            capo_network_firewall.types.action_scope.deserialize_aws_json_1_0(
                data["ActionScope"]
            )
        )
    else:
        import typing

        out["action_scope"] = typing.cast(
            "capo_network_firewall.types.action_scope.ActionScope", ""
        )
    if data.get("Hook") is not None:
        import capo_network_firewall.types.hook_key

        out["hook"] = capo_network_firewall.types.hook_key.deserialize_aws_json_1_0(
            data["Hook"]
        )
    else:
        import typing

        out["hook"] = typing.cast("capo_network_firewall.types.hook_key.HookKey", "")
    if data.get("Protocol") is not None:
        import capo_network_firewall.types.firewall_rule_protocol

        out["protocol"] = (
            capo_network_firewall.types.firewall_rule_protocol.deserialize_aws_json_1_0(
                data["Protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_network_firewall.types.firewall_rule_protocol.FirewallRuleProtocol",
            "",
        )
    if data.get("SourceIPs") is not None:
        out["source_i_ps"] = data["SourceIPs"]
    if data.get("DestIPs") is not None:
        out["dest_i_ps"] = data["DestIPs"]
    if data.get("SourcePorts") is not None:
        out["source_ports"] = data["SourcePorts"]
    if data.get("DestPorts") is not None:
        out["dest_ports"] = data["DestPorts"]
    if data.get("RuleOptions") is not None:
        import capo_network_firewall.types.rule_options

        out["rule_options"] = (
            capo_network_firewall.types.rule_options.deserialize_aws_json_1_0(
                data["RuleOptions"]
            )
        )
    if data.get("AcceptPriorHooks") is not None:
        out["accept_prior_hooks"] = data["AcceptPriorHooks"]
    if data.get("AlertEnabled") is not None:
        out["alert_enabled"] = data["AlertEnabled"]
    if data.get("BypassIPSEnabled") is not None:
        out["bypass_ips_enabled"] = data["BypassIPSEnabled"]
    if data.get("RuleMetadata") is not None:
        import capo_network_firewall.types.rule_metadata

        out["rule_metadata"] = (
            capo_network_firewall.types.rule_metadata.deserialize_aws_json_1_0(
                data["RuleMetadata"]
            )
        )
    return out
