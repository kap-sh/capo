"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.ip_address
    import capo_networkmanager.types.nat_rule_number


class NatRuleRequest(TypedDict, closed=True):
    rule_number: "capo_networkmanager.types.nat_rule_number.NatRuleNumber"
    """<p>The rule number, from 1 to 32766. Each rule number must be unique for the attachment.</p>"""
    match_source_cidr: "capo_networkmanager.types.ip_address.IPAddress"
    """<p>The IPv4 CIDR block to match against the source address of traffic from the attachment. The CIDR block can't overlap with the multicast range (224.0.0.0/4).</p>"""
    nat_cidr: "capo_networkmanager.types.ip_address.IPAddress"
    """<p>The IPv4 CIDR block to translate matching source addresses to. The prefix length must be the same as the prefix length of <code>MatchSourceCidr</code>. The CIDR block must be within a private (RFC 1918) or shared address space (RFC 6598) range. The CIDR blocks of the NAT rules of an attachment can't overlap with each other.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NatRuleRequest) -> dict:
    out: dict = {}
    out["RuleNumber"] = value["rule_number"]
    out["MatchSourceCidr"] = value["match_source_cidr"]
    out["NatCidr"] = value["nat_cidr"]
    return out


def deserialize_json(data: dict) -> NatRuleRequest:
    out: NatRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleNumber") is not None:
        out["rule_number"] = data["RuleNumber"]
    else:
        out["rule_number"] = 0
    if data.get("MatchSourceCidr") is not None:
        out["match_source_cidr"] = data["MatchSourceCidr"]
    else:
        out["match_source_cidr"] = ""
    if data.get("NatCidr") is not None:
        out["nat_cidr"] = data["NatCidr"]
    else:
        out["nat_cidr"] = ""
    return out
