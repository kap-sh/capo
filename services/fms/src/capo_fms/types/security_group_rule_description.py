"""Generated from Smithy shape ``com.amazonaws.fms#SecurityGroupRuleDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.cidr
    import capo_fms.types.ip_port_number
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id


class SecurityGroupRuleDescription(TypedDict, closed=True):
    ipv4_range: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>The IPv4 ranges for the security group rule.</p>"""
    ipv6_range: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>The IPv6 ranges for the security group rule.</p>"""
    prefix_list_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the prefix list for the security group rule.</p>"""
    protocol: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number.</p>"""
    from_port: NotRequired["capo_fms.types.ip_port_number.IPPortNumber"]
    """<p>The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of <code>-1</code> indicates all ICMP/ICMPv6 types.</p>"""
    to_port: NotRequired["capo_fms.types.ip_port_number.IPPortNumber"]
    """<p>The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of <code>-1</code> indicates all ICMP/ICMPv6 codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupRuleDescription) -> dict:
    out: dict = {}
    if "ipv4_range" in value:
        out["IPV4Range"] = value["ipv4_range"]
    if "ipv6_range" in value:
        out["IPV6Range"] = value["ipv6_range"]
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupRuleDescription:
    out: SecurityGroupRuleDescription = {}  # type: ignore[typeddict-item]
    if data.get("IPV4Range") is not None:
        out["ipv4_range"] = data["IPV4Range"]
    if data.get("IPV6Range") is not None:
        out["ipv6_range"] = data["IPV6Range"]
    if data.get("PrefixListId") is not None:
        out["prefix_list_id"] = data["PrefixListId"]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupRuleDescription) -> dict:
    out: dict = {}
    if "ipv4_range" in value:
        out["IPV4Range"] = value["ipv4_range"]
    if "ipv6_range" in value:
        out["IPV6Range"] = value["ipv6_range"]
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_cbor(data: dict) -> SecurityGroupRuleDescription:
    out: SecurityGroupRuleDescription = {}  # type: ignore[typeddict-item]
    if data.get("IPV4Range") is not None:
        out["ipv4_range"] = data["IPV4Range"]
    if data.get("IPV6Range") is not None:
        out["ipv6_range"] = data["IPV6Range"]
    if data.get("PrefixListId") is not None:
        out["prefix_list_id"] = data["PrefixListId"]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    return out
