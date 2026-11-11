"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_rule_group_entries
    import capo_network_firewall.types.ips_rule_group_entries
    import capo_network_firewall.types.policy_default_action
    import capo_network_firewall.types.policy_mode
    import capo_network_firewall.types.policy_variables
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.route53_resolved_ip_validation
    import capo_network_firewall.types.stateful_engine_options_v2


class FirewallPolicyV2(TypedDict, closed=True):
    firewall_rule_group_entries: NotRequired[
        "capo_network_firewall.types.firewall_rule_group_entries.FirewallRuleGroupEntries"
    ]
    """<p>The firewall section of the policy—the rule groups that the firewall engine evaluates. Each entry references an existing firewall engine rule group or embeds a rule group directly in the policy, and each entry has a unique priority that sets its evaluation order within the section.</p>"""
    ips_rule_group_entries: NotRequired[
        "capo_network_firewall.types.ips_rule_group_entries.IpsRuleGroupEntries"
    ]
    """<p>The IPS section of the policy—the rule groups that the IPS engine evaluates. Each entry references an existing IPS engine rule group or embeds a rule group directly in the policy. IPS section entries don't use a priority.</p>"""
    policy_mode: NotRequired["capo_network_firewall.types.policy_mode.PolicyMode"]
    """<p>Indicates whether the policy's engines enforce their verdicts or only report them. In <code>ENFORCE</code> mode, the firewall engine and IPS engine apply their verdicts to traffic. In <code>MONITOR</code> mode, the engines evaluate traffic and generate logs and metrics, but don't block traffic, so you can observe how a policy would behave before you enforce it. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies-v2.html">Next Generation policies</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    firewall_default_action: NotRequired[
        "capo_network_firewall.types.policy_default_action.PolicyDefaultAction"
    ]
    """<p>The action that the firewall engine takes on traffic that doesn't match any firewall engine rule at a hook. The firewall engine is drop by default. You can set the default action to one of the following:</p> <ul> <li> <p> <code>DROP</code> - Block the traffic.</p> </li> <li> <p> <code>ACCEPT</code> - Allow the traffic.</p> </li> <li> <p> <code>REJECT</code> - Block the traffic and send a TCP reset packet back to the client.</p> </li> <li> <p> <code>ALERT</code> - Allow the traffic and generate an alert log for the traffic that reaches the default action at every hook. This is distinct from setting the policy mode to <code>MONITOR</code>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies-v2.html">Next Generation policies</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    stateful_engine_options: NotRequired[
        "capo_network_firewall.types.stateful_engine_options_v2.StatefulEngineOptionsV2"
    ]
    """<p>Additional options governing how the engines handle stateful traffic, such as the stream exception policy and flow timeouts.</p>"""
    tls_inspection_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration to use to decrypt traffic for inspection. Next Generation policies support session holding only. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    policy_variables: NotRequired[
        "capo_network_firewall.types.policy_variables.PolicyVariables"
    ]
    """<p>Contains variables that you can use to override default Suricata settings in your Next Generation policy.</p>"""
    route53_resolved_ip_validation: NotRequired[
        "capo_network_firewall.types.route53_resolved_ip_validation.Route53ResolvedIPValidation"
    ]
    """<p>The settings that enable resolved IP validation for the Next Generation policy. Resolved IP validation verifies that a connection's destination IP address is one that the Amazon Route 53 Resolver returned in a DNS response for a domain. A VPC that's associated with the Route 53 Resolver DNS Firewall rule group that you specify must send the response. This checks how the destination IP address was obtained, instead of relying only on the domain that the client asserts in its TLS Server Name Indication (SNI) or HTTP <code>Host</code> header. For more information, see <a>Route53ResolvedIPValidation</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyV2) -> dict:
    out: dict = {}
    if "firewall_rule_group_entries" in value:
        import capo_network_firewall.types.firewall_rule_group_entries

        out["FirewallRuleGroupEntries"] = (
            capo_network_firewall.types.firewall_rule_group_entries.serialize_aws_json_1_0(
                value["firewall_rule_group_entries"]
            )
        )
    if "ips_rule_group_entries" in value:
        import capo_network_firewall.types.ips_rule_group_entries

        out["IpsRuleGroupEntries"] = (
            capo_network_firewall.types.ips_rule_group_entries.serialize_aws_json_1_0(
                value["ips_rule_group_entries"]
            )
        )
    if "policy_mode" in value:
        import capo_network_firewall.types.policy_mode

        out["PolicyMode"] = (
            capo_network_firewall.types.policy_mode.serialize_aws_json_1_0(
                value["policy_mode"]
            )
        )
    if "firewall_default_action" in value:
        import capo_network_firewall.types.policy_default_action

        out["FirewallDefaultAction"] = (
            capo_network_firewall.types.policy_default_action.serialize_aws_json_1_0(
                value["firewall_default_action"]
            )
        )
    if "stateful_engine_options" in value:
        import capo_network_firewall.types.stateful_engine_options_v2

        out["StatefulEngineOptions"] = (
            capo_network_firewall.types.stateful_engine_options_v2.serialize_aws_json_1_0(
                value["stateful_engine_options"]
            )
        )
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "policy_variables" in value:
        import capo_network_firewall.types.policy_variables

        out["PolicyVariables"] = (
            capo_network_firewall.types.policy_variables.serialize_aws_json_1_0(
                value["policy_variables"]
            )
        )
    if "route53_resolved_ip_validation" in value:
        import capo_network_firewall.types.route53_resolved_ip_validation

        out["Route53ResolvedIPValidation"] = (
            capo_network_firewall.types.route53_resolved_ip_validation.serialize_aws_json_1_0(
                value["route53_resolved_ip_validation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyV2:
    out: FirewallPolicyV2 = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupEntries") is not None:
        import capo_network_firewall.types.firewall_rule_group_entries

        out["firewall_rule_group_entries"] = (
            capo_network_firewall.types.firewall_rule_group_entries.deserialize_aws_json_1_0(
                data["FirewallRuleGroupEntries"]
            )
        )
    if data.get("IpsRuleGroupEntries") is not None:
        import capo_network_firewall.types.ips_rule_group_entries

        out["ips_rule_group_entries"] = (
            capo_network_firewall.types.ips_rule_group_entries.deserialize_aws_json_1_0(
                data["IpsRuleGroupEntries"]
            )
        )
    if data.get("PolicyMode") is not None:
        import capo_network_firewall.types.policy_mode

        out["policy_mode"] = (
            capo_network_firewall.types.policy_mode.deserialize_aws_json_1_0(
                data["PolicyMode"]
            )
        )
    if data.get("FirewallDefaultAction") is not None:
        import capo_network_firewall.types.policy_default_action

        out["firewall_default_action"] = (
            capo_network_firewall.types.policy_default_action.deserialize_aws_json_1_0(
                data["FirewallDefaultAction"]
            )
        )
    if data.get("StatefulEngineOptions") is not None:
        import capo_network_firewall.types.stateful_engine_options_v2

        out["stateful_engine_options"] = (
            capo_network_firewall.types.stateful_engine_options_v2.deserialize_aws_json_1_0(
                data["StatefulEngineOptions"]
            )
        )
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if data.get("PolicyVariables") is not None:
        import capo_network_firewall.types.policy_variables

        out["policy_variables"] = (
            capo_network_firewall.types.policy_variables.deserialize_aws_json_1_0(
                data["PolicyVariables"]
            )
        )
    if data.get("Route53ResolvedIPValidation") is not None:
        import capo_network_firewall.types.route53_resolved_ip_validation

        out["route53_resolved_ip_validation"] = (
            capo_network_firewall.types.route53_resolved_ip_validation.deserialize_aws_json_1_0(
                data["Route53ResolvedIPValidation"]
            )
        )
    return out
