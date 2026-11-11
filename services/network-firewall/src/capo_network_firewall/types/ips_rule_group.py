"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IpsRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.ips_rules_source
    import capo_network_firewall.types.reference_sets
    import capo_network_firewall.types.rule_variables


class IpsRuleGroup(TypedDict, closed=True):
    rules_source: "capo_network_firewall.types.ips_rules_source.IpsRulesSource"
    """<p>The stateful inspection criteria for the IPS engine rule group.</p>"""
    rule_variables: NotRequired[
        "capo_network_firewall.types.rule_variables.RuleVariables"
    ]
    """<p>Settings that are available for use in the rules in the IPS engine rule group.</p>"""
    reference_sets: NotRequired[
        "capo_network_firewall.types.reference_sets.ReferenceSets"
    ]
    """<p>The list of a rule group's reference sets.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IpsRuleGroup) -> dict:
    out: dict = {}
    import capo_network_firewall.types.ips_rules_source

    out["RulesSource"] = (
        capo_network_firewall.types.ips_rules_source.serialize_aws_json_1_0(
            value["rules_source"]
        )
    )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> IpsRuleGroup:
    out: IpsRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RulesSource") is not None:
        import capo_network_firewall.types.ips_rules_source

        out["rules_source"] = (
            capo_network_firewall.types.ips_rules_source.deserialize_aws_json_1_0(
                data["RulesSource"]
            )
        )
    else:
        raise DeserializationError("IpsRuleGroup.rules_source required")
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
    return out
