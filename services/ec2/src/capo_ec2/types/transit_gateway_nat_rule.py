"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayNatRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_nat_rule_state


class TransitGatewayNatRule(TypedDict, closed=True):
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number.</p>"""
    match_source_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block of the source addresses to translate.</p>"""
    nat_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block that the transit gateway translates the source addresses to.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_nat_rule_state.TransitGatewayNatRuleState"
    ]
    """<p>The state of the NAT gateway rule. The possible values are:</p> <ul> <li> <p> <code>pending</code> - The transit gateway is applying a change to the rule.</p> </li> <li> <p> <code>activated</code> - The rule is in effect because NAT gateway support is enabled for the attachment.</p> </li> <li> <p> <code>deactivated</code> - The rule isn't in effect because NAT gateway support is disabled for the attachment.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayNatRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))
    if "match_source_cidr" in value:
        pairs.append((f"{key_prefix}MatchSourceCidr", str(value["match_source_cidr"])))
    if "nat_cidr" in value:
        pairs.append((f"{key_prefix}NatCidr", str(value["nat_cidr"])))
    if "state" in value:
        import capo_ec2.types.transit_gateway_nat_rule_state

        capo_ec2.types.transit_gateway_nat_rule_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayNatRule:
    out: TransitGatewayNatRule = {}  # type: ignore[typeddict-item]
    child_rule_number = el.find("ruleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_match_source_cidr = el.find("matchSourceCidr")
    if child_match_source_cidr is not None:
        out["match_source_cidr"] = str(child_match_source_cidr.text or "")
    child_nat_cidr = el.find("natCidr")
    if child_nat_cidr is not None:
        out["nat_cidr"] = str(child_nat_cidr.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_nat_rule_state

        out["state"] = (
            capo_ec2.types.transit_gateway_nat_rule_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
