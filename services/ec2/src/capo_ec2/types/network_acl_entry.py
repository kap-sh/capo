"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.icmp_type_code
    import capo_ec2.types.integer
    import capo_ec2.types.port_range
    import capo_ec2.types.rule_action
    import capo_ec2.types.string


class NetworkAclEntry(TypedDict, closed=True):
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 network range to allow or deny, in CIDR notation.</p>"""
    egress: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the rule is an egress rule (applied to traffic leaving the subnet).</p>"""
    icmp_type_code: NotRequired["capo_ec2.types.icmp_type_code.IcmpTypeCode"]
    """<p>ICMP protocol: The ICMP type and code.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 network range to allow or deny, in CIDR notation.</p>"""
    port_range: NotRequired["capo_ec2.types.port_range.PortRange"]
    """<p>TCP or UDP protocols: The range of ports the rule applies to.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol number. A value of "-1" means all protocols.</p>"""
    rule_action: NotRequired["capo_ec2.types.rule_action.RuleAction"]
    """<p>Indicates whether to allow or deny the traffic that matches the rule.</p>"""
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number for the entry. ACL entries are processed in ascending order by rule number.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkAclEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr_block" in value:
        pairs.append((f"{key_prefix}CidrBlock", str(value["cidr_block"])))
    if "egress" in value:
        pairs.append((f"{key_prefix}Egress", "true" if value["egress"] else "false"))
    if "icmp_type_code" in value:
        import capo_ec2.types.icmp_type_code

        capo_ec2.types.icmp_type_code.serialize_ec2_query(
            value["icmp_type_code"], pairs, f"{key_prefix}IcmpTypeCode"
        )
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "port_range" in value:
        import capo_ec2.types.port_range

        capo_ec2.types.port_range.serialize_ec2_query(
            value["port_range"], pairs, f"{key_prefix}PortRange"
        )
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "rule_action" in value:
        import capo_ec2.types.rule_action

        capo_ec2.types.rule_action.serialize_ec2_query(
            value["rule_action"], pairs, f"{key_prefix}RuleAction"
        )
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))


def deserialize_ec2_query(el: Element) -> NetworkAclEntry:
    out: NetworkAclEntry = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("cidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_egress = el.find("egress")
    if child_egress is not None:
        out["egress"] = (child_egress.text or "").lower() == "true"
    child_icmp_type_code = el.find("icmpTypeCode")
    if child_icmp_type_code is not None:
        import capo_ec2.types.icmp_type_code

        out["icmp_type_code"] = capo_ec2.types.icmp_type_code.deserialize_ec2_query(
            child_icmp_type_code
        )
    child_ipv6_cidr_block = el.find("ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_port_range = el.find("portRange")
    if child_port_range is not None:
        import capo_ec2.types.port_range

        out["port_range"] = capo_ec2.types.port_range.deserialize_ec2_query(
            child_port_range
        )
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_rule_action = el.find("ruleAction")
    if child_rule_action is not None:
        import capo_ec2.types.rule_action

        out["rule_action"] = capo_ec2.types.rule_action.deserialize_ec2_query(
            child_rule_action
        )
    child_rule_number = el.find("ruleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    return out
