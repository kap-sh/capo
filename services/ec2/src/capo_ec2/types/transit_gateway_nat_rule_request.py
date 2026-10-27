"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayNatRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class TransitGatewayNatRuleRequest(TypedDict, closed=True):
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number. Valid values are 1 to 32766. Each rule number must be unique within the request.</p>"""
    match_source_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block of the source addresses to translate. The CIDR block can't overlap the multicast range (<code>224.0.0.0/4</code>) or the link-local range (<code>169.254.0.0/16</code>).</p>"""
    nat_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block to translate the source addresses to. The CIDR block must be in a private (RFC 1918) or shared address space (RFC 6598) range, and must have the same prefix length as <code>MatchSourceCidr</code>. The CIDR blocks in the rules for an attachment can't overlap each other.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayNatRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))
    if "match_source_cidr" in value:
        pairs.append((f"{key_prefix}MatchSourceCidr", str(value["match_source_cidr"])))
    if "nat_cidr" in value:
        pairs.append((f"{key_prefix}NatCidr", str(value["nat_cidr"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayNatRuleRequest:
    out: TransitGatewayNatRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_match_source_cidr = el.find("MatchSourceCidr")
    if child_match_source_cidr is not None:
        out["match_source_cidr"] = str(child_match_source_cidr.text or "")
    child_nat_cidr = el.find("NatCidr")
    if child_nat_cidr is not None:
        out["nat_cidr"] = str(child_nat_cidr.text or "")
    return out
