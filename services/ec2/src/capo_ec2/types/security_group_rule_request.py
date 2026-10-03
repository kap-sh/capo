"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.security_group_id
    import capo_ec2.types.string


class SecurityGroupRuleRequest(TypedDict, closed=True):
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a>). </p> <p>Use <code>-1</code> to specify all protocols.</p>"""
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p>"""
    cidr_ipv4: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR range. To specify a single IPv4 address, use the /32 prefix length. </p>"""
    cidr_ipv6: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.</p>"""
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    referenced_group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group that is referenced in the security group rule.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ip_protocol" in value:
        pairs.append((f"{key_prefix}IpProtocol", str(value["ip_protocol"])))
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))
    if "cidr_ipv4" in value:
        pairs.append((f"{key_prefix}CidrIpv4", str(value["cidr_ipv4"])))
    if "cidr_ipv6" in value:
        pairs.append((f"{key_prefix}CidrIpv6", str(value["cidr_ipv6"])))
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "referenced_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReferencedGroupId", str(value["referenced_group_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleRequest:
    out: SecurityGroupRuleRequest = {}  # type: ignore[typeddict-item]
    child_ip_protocol = el.find("IpProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_cidr_ipv4 = el.find("CidrIpv4")
    if child_cidr_ipv4 is not None:
        out["cidr_ipv4"] = str(child_cidr_ipv4.text or "")
    child_cidr_ipv6 = el.find("CidrIpv6")
    if child_cidr_ipv6 is not None:
        out["cidr_ipv6"] = str(child_cidr_ipv6.text or "")
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_referenced_group_id = el.find("ReferencedGroupId")
    if child_referenced_group_id is not None:
        out["referenced_group_id"] = str(child_referenced_group_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
