"""Generated from Smithy shape ``com.amazonaws.ec2#IpPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.ip_range_list
    import capo_ec2.types.ipv6_range_list
    import capo_ec2.types.prefix_list_id_list
    import capo_ec2.types.string
    import capo_ec2.types.user_id_group_pair_list


class IpPermission(TypedDict, closed=True):
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a>).</p> <p>Use <code>-1</code> to specify all protocols. When authorizing security group rules, specifying <code>-1</code> or a protocol number other than <code>tcp</code>, <code>udp</code>, <code>icmp</code>, or <code>icmpv6</code> allows traffic on all ports, regardless of any port range you specify. For <code>tcp</code>, <code>udp</code>, and <code>icmp</code>, you must specify a port range. For <code>icmpv6</code>, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.</p>"""
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p>"""
    user_id_group_pairs: NotRequired[
        "capo_ec2.types.user_id_group_pair_list.UserIdGroupPairList"
    ]
    """<p>The security group and Amazon Web Services account ID pairs.</p>"""
    ip_ranges: NotRequired["capo_ec2.types.ip_range_list.IpRangeList"]
    """<p>The IPv4 address ranges.</p>"""
    ipv6_ranges: NotRequired["capo_ec2.types.ipv6_range_list.Ipv6RangeList"]
    """<p>The IPv6 address ranges.</p>"""
    prefix_list_ids: NotRequired["capo_ec2.types.prefix_list_id_list.PrefixListIdList"]
    """<p>The prefix list IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ip_protocol" in value:
        pairs.append((f"{key_prefix}IpProtocol", str(value["ip_protocol"])))
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))
    if "user_id_group_pairs" in value:
        import capo_ec2.types.user_id_group_pair_list

        capo_ec2.types.user_id_group_pair_list.serialize_ec2_query(
            value["user_id_group_pairs"], pairs, f"{key_prefix}Groups"
        )
    if "ip_ranges" in value:
        import capo_ec2.types.ip_range_list

        capo_ec2.types.ip_range_list.serialize_ec2_query(
            value["ip_ranges"], pairs, f"{key_prefix}IpRanges"
        )
    if "ipv6_ranges" in value:
        import capo_ec2.types.ipv6_range_list

        capo_ec2.types.ipv6_range_list.serialize_ec2_query(
            value["ipv6_ranges"], pairs, f"{key_prefix}Ipv6Ranges"
        )
    if "prefix_list_ids" in value:
        import capo_ec2.types.prefix_list_id_list

        capo_ec2.types.prefix_list_id_list.serialize_ec2_query(
            value["prefix_list_ids"], pairs, f"{key_prefix}PrefixListIds"
        )


def deserialize_ec2_query(el: Element) -> IpPermission:
    out: IpPermission = {}  # type: ignore[typeddict-item]
    child_ip_protocol = el.find("ipProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_from_port = el.find("fromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("toPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_user_id_group_pairs = el.find("groups")
    if child_user_id_group_pairs is not None:
        import capo_ec2.types.user_id_group_pair_list

        out["user_id_group_pairs"] = (
            capo_ec2.types.user_id_group_pair_list.deserialize_ec2_query(
                child_user_id_group_pairs
            )
        )
    child_ip_ranges = el.find("ipRanges")
    if child_ip_ranges is not None:
        import capo_ec2.types.ip_range_list

        out["ip_ranges"] = capo_ec2.types.ip_range_list.deserialize_ec2_query(
            child_ip_ranges
        )
    child_ipv6_ranges = el.find("ipv6Ranges")
    if child_ipv6_ranges is not None:
        import capo_ec2.types.ipv6_range_list

        out["ipv6_ranges"] = capo_ec2.types.ipv6_range_list.deserialize_ec2_query(
            child_ipv6_ranges
        )
    child_prefix_list_ids = el.find("prefixListIds")
    if child_prefix_list_ids is not None:
        import capo_ec2.types.prefix_list_id_list

        out["prefix_list_ids"] = (
            capo_ec2.types.prefix_list_id_list.deserialize_ec2_query(
                child_prefix_list_ids
            )
        )
    return out
