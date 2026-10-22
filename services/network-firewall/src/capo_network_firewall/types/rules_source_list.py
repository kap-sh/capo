"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RulesSourceList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.generated_rules_type
    import capo_network_firewall.types.rule_targets
    import capo_network_firewall.types.target_types


class RulesSourceList(TypedDict, closed=True):
    targets: "capo_network_firewall.types.rule_targets.RuleTargets"
    """<p>The domains that you want to inspect for in your traffic flows. Valid domain specifications are the following:</p> <ul> <li> <p>Explicit names. For example, <code>abc.example.com</code> matches only the domain <code>abc.example.com</code>.</p> </li> <li> <p>Names that use a domain wildcard, which you indicate with an initial '<code>.</code>'. For example,<code>.example.com</code> matches <code>example.com</code> and matches all subdomains of <code>example.com</code>, such as <code>abc.example.com</code> and <code>www.example.com</code>. </p> </li> </ul>"""
    target_types: "capo_network_firewall.types.target_types.TargetTypes"
    """<p>The types of matching to perform against the domains in <code>Targets</code>. You can specify any combination of the following:</p> <ul> <li> <p> <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> – Match the domain against the domain that the Amazon Route 53 Resolver resolved the connection's destination IP address for.</p> </li> <li> <p> <code>HTTP_HOST</code> – Match the domain against the <code>Host</code> header of HTTP traffic.</p> </li> <li> <p> <code>TLS_SNI</code> – Match the domain against the Server Name Indication (SNI) of HTTPS traffic.</p> </li> </ul> <p> <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> matches on how the destination IP address was resolved, rather than on the domain that the client asserts in its TLS SNI or HTTP <code>Host</code> header. This target type takes effect when you configure resolved IP validation on the firewall policy. For more information, see <a>Route53ResolvedIPValidation</a>.</p> <p>Whether you include <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> changes what the generated rules match, together with <code>GeneratedRulesType</code>:</p> <ul> <li> <p>Combining <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> with <code>TLS_SNI</code> or <code>HTTP_HOST</code> in an <code>ALLOWLIST</code> requires both conditions to match. The SNI or <code>Host</code> header must match the domain, <b>and</b> the Route 53 Resolver must have resolved the destination IP address for that domain. Network Firewall allows traffic only in that case. Traffic that matches one condition, such as a spoofed <code>Host</code> header sent to an unresolved IP address, is not allowed.</p> </li> <li> <p>In a <code>DENYLIST</code>, or when <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> is the only target type, Network Firewall evaluates each condition independently: a match on either the domain (SNI or <code>Host</code>) or the resolved destination IP address triggers the rule.</p> </li> <li> <p>When you don't include <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code>, the generated rules match only on the SNI or <code>Host</code> header, without checking how the destination IP address was resolved.</p> </li> </ul> <p>An <code>ALLOWLIST</code> whose only target type is <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> is additive: it allows matching traffic but doesn't generate a default rule that drops non-matching traffic. Only the <code>TLS_SNI</code> and <code>HTTP_HOST</code> target types generate that default drop. To allow only the resolved domains and drop all other traffic, include a protocol target type as well.</p>"""
    generated_rules_type: (
        "capo_network_firewall.types.generated_rules_type.GeneratedRulesType"
    )
    """<p>Whether you want to apply allow, reject, alert, or drop behavior to the domains in your target list.</p> <note> <p>When logging is enabled and you choose Alert, traffic that matches the domain specifications generates an alert in the firewall's logs. Then, traffic either passes, is rejected, or drops based on other rules in the firewall policy.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RulesSourceList) -> dict:
    out: dict = {}
    import capo_network_firewall.types.rule_targets

    out["Targets"] = capo_network_firewall.types.rule_targets.serialize_aws_json_1_0(
        value["targets"]
    )
    import capo_network_firewall.types.target_types

    out["TargetTypes"] = (
        capo_network_firewall.types.target_types.serialize_aws_json_1_0(
            value["target_types"]
        )
    )
    import capo_network_firewall.types.generated_rules_type

    out["GeneratedRulesType"] = (
        capo_network_firewall.types.generated_rules_type.serialize_aws_json_1_0(
            value["generated_rules_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RulesSourceList:
    out: RulesSourceList = {}  # type: ignore[typeddict-item]
    if data.get("Targets") is not None:
        import capo_network_firewall.types.rule_targets

        out["targets"] = (
            capo_network_firewall.types.rule_targets.deserialize_aws_json_1_0(
                data["Targets"]
            )
        )
    else:
        out["targets"] = []
    if data.get("TargetTypes") is not None:
        import capo_network_firewall.types.target_types

        out["target_types"] = (
            capo_network_firewall.types.target_types.deserialize_aws_json_1_0(
                data["TargetTypes"]
            )
        )
    else:
        out["target_types"] = []
    if data.get("GeneratedRulesType") is not None:
        import capo_network_firewall.types.generated_rules_type

        out["generated_rules_type"] = (
            capo_network_firewall.types.generated_rules_type.deserialize_aws_json_1_0(
                data["GeneratedRulesType"]
            )
        )
    else:
        import typing

        out["generated_rules_type"] = typing.cast(
            "capo_network_firewall.types.generated_rules_type.GeneratedRulesType", ""
        )
    return out
