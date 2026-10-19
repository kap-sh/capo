"""Generated from Smithy shape ``com.amazonaws.finspace#NetworkACLEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.icmp_type_code
    import capo_finspace.types.port_range
    import capo_finspace.types.protocol
    import capo_finspace.types.rule_action
    import capo_finspace.types.rule_number
    import capo_finspace.types.valid_cidr_block


class NetworkACLEntry(TypedDict, closed=True):
    rule_number: "capo_finspace.types.rule_number.RuleNumber"
    """<p> The rule number for the entry. For example <i>100</i>. All the network ACL entries are processed in ascending order by rule number. </p>"""
    protocol: "capo_finspace.types.protocol.Protocol"
    """<p> The protocol number. A value of <i>-1</i> means all the protocols. </p>"""
    rule_action: "capo_finspace.types.rule_action.RuleAction"
    """<p> Indicates whether to allow or deny the traffic that matches the rule. </p>"""
    port_range: NotRequired["capo_finspace.types.port_range.PortRange"]
    """<p> The range of ports the rule applies to. </p>"""
    icmp_type_code: NotRequired["capo_finspace.types.icmp_type_code.IcmpTypeCode"]
    """<p> Defines the ICMP protocol that consists of the ICMP type and code. </p>"""
    cidr_block: "capo_finspace.types.valid_cidr_block.ValidCIDRBlock"
    """<p> The IPv4 network range to allow or deny, in CIDR notation. For example, <code>172.16.0.0/24</code>. We modify the specified CIDR block to its canonical form. For example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkACLEntry) -> dict:
    out: dict = {}
    out["ruleNumber"] = value["rule_number"]
    out["protocol"] = value["protocol"]
    import capo_finspace.types.rule_action

    out["ruleAction"] = capo_finspace.types.rule_action.serialize_json(
        value["rule_action"]
    )
    if "port_range" in value:
        import capo_finspace.types.port_range

        out["portRange"] = capo_finspace.types.port_range.serialize_json(
            value["port_range"]
        )
    if "icmp_type_code" in value:
        import capo_finspace.types.icmp_type_code

        out["icmpTypeCode"] = capo_finspace.types.icmp_type_code.serialize_json(
            value["icmp_type_code"]
        )
    out["cidrBlock"] = value["cidr_block"]
    return out


def deserialize_json(data: dict) -> NetworkACLEntry:
    out: NetworkACLEntry = {}  # type: ignore[typeddict-item]
    if data.get("ruleNumber") is not None:
        out["rule_number"] = data["ruleNumber"]
    else:
        out["rule_number"] = 0
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    else:
        out["protocol"] = ""
    if data.get("ruleAction") is not None:
        import capo_finspace.types.rule_action

        out["rule_action"] = capo_finspace.types.rule_action.deserialize_json(
            data["ruleAction"]
        )
    else:
        import typing

        out["rule_action"] = typing.cast(
            "capo_finspace.types.rule_action.RuleAction", ""
        )
    if data.get("portRange") is not None:
        import capo_finspace.types.port_range

        out["port_range"] = capo_finspace.types.port_range.deserialize_json(
            data["portRange"]
        )
    if data.get("icmpTypeCode") is not None:
        import capo_finspace.types.icmp_type_code

        out["icmp_type_code"] = capo_finspace.types.icmp_type_code.deserialize_json(
            data["icmpTypeCode"]
        )
    if data.get("cidrBlock") is not None:
        out["cidr_block"] = data["cidrBlock"]
    else:
        out["cidr_block"] = ""
    return out
