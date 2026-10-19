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
    """<p>The protocols you want to inspect. Specify <code>TLS_SNI</code> for <code>HTTPS</code>. Specify <code>HTTP_HOST</code> for <code>HTTP</code>. You can specify either or both. </p>"""
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
