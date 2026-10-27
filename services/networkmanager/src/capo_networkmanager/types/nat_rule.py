"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.ip_address
    import capo_networkmanager.types.nat_rule_number
    import capo_networkmanager.types.nat_rule_state


class NatRule(TypedDict, closed=True):
    rule_number: NotRequired["capo_networkmanager.types.nat_rule_number.NatRuleNumber"]
    """<p>The rule number. Rule numbers identify the rules of an attachment and don't set the order in which rules are evaluated.</p>"""
    match_source_cidr: NotRequired["capo_networkmanager.types.ip_address.IPAddress"]
    """<p>The source CIDR block that the rule matches for traffic from the attachment.</p>"""
    nat_cidr: NotRequired["capo_networkmanager.types.ip_address.IPAddress"]
    """<p>The CIDR block that matching source addresses are translated to.</p>"""
    state: NotRequired["capo_networkmanager.types.nat_rule_state.NatRuleState"]
    """<p>The state of the NAT rule. The possible values are the following:</p> <ul> <li> <p> <code>CREATING</code>: The rule is being created.</p> </li> <li> <p> <code>MODIFYING</code>: The rule is being modified.</p> </li> <li> <p> <code>DELETING</code>: The rule is being deleted.</p> </li> <li> <p> <code>ACTIVATING</code>: NAT gateway support is being enabled, and the rule is being applied.</p> </li> <li> <p> <code>ACTIVATED</code>: NAT gateway support is enabled, and the rule is applied.</p> </li> <li> <p> <code>DEACTIVATING</code>: NAT gateway support is being disabled, and the rule is being removed from use.</p> </li> <li> <p> <code>DEACTIVATED</code>: NAT gateway support is disabled, and the rule isn't applied.</p> </li> <li> <p> <code>FAILED</code>: The attachment failed to be created, and the rule isn't applied.</p> </li> <li> <p> <code>PENDING_ATTACHMENT_ACCEPTANCE</code>: The attachment is pending acceptance. The rule is applied after the attachment is accepted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: NatRule) -> dict:
    out: dict = {}
    if "rule_number" in value:
        out["RuleNumber"] = value["rule_number"]
    if "match_source_cidr" in value:
        out["MatchSourceCidr"] = value["match_source_cidr"]
    if "nat_cidr" in value:
        out["NatCidr"] = value["nat_cidr"]
    if "state" in value:
        import capo_networkmanager.types.nat_rule_state

        out["State"] = capo_networkmanager.types.nat_rule_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> NatRule:
    out: NatRule = {}  # type: ignore[typeddict-item]
    if data.get("RuleNumber") is not None:
        out["rule_number"] = data["RuleNumber"]
    if data.get("MatchSourceCidr") is not None:
        out["match_source_cidr"] = data["MatchSourceCidr"]
    if data.get("NatCidr") is not None:
        out["nat_cidr"] = data["NatCidr"]
    if data.get("State") is not None:
        import capo_networkmanager.types.nat_rule_state

        out["state"] = capo_networkmanager.types.nat_rule_state.deserialize_json(
            data["State"]
        )
    return out
