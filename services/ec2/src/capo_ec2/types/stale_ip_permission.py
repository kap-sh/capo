"""Generated from Smithy shape ``com.amazonaws.ec2#StaleIpPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.ip_ranges
    import capo_ec2.types.prefix_list_id_set
    import capo_ec2.types.string
    import capo_ec2.types.user_id_group_pair_set


class StaleIpPermission(TypedDict, closed=True):
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers)</a>.</p>"""
    ip_ranges: NotRequired["capo_ec2.types.ip_ranges.IpRanges"]
    """<p>The IP ranges. Not applicable for stale security group rules.</p>"""
    prefix_list_ids: NotRequired["capo_ec2.types.prefix_list_id_set.PrefixListIdSet"]
    """<p>The prefix list IDs. Not applicable for stale security group rules.</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes).</p>"""
    user_id_group_pairs: NotRequired[
        "capo_ec2.types.user_id_group_pair_set.UserIdGroupPairSet"
    ]
    """<p>The security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StaleIpPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "ip_protocol" in value:
        pairs.append((f"{key_prefix}IpProtocol", str(value["ip_protocol"])))
    if "ip_ranges" in value:
        import capo_ec2.types.ip_ranges

        capo_ec2.types.ip_ranges.serialize_ec2_query(
            value["ip_ranges"], pairs, f"{key_prefix}IpRanges"
        )
    if "prefix_list_ids" in value:
        import capo_ec2.types.prefix_list_id_set

        capo_ec2.types.prefix_list_id_set.serialize_ec2_query(
            value["prefix_list_ids"], pairs, f"{key_prefix}PrefixListIds"
        )
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))
    if "user_id_group_pairs" in value:
        import capo_ec2.types.user_id_group_pair_set

        capo_ec2.types.user_id_group_pair_set.serialize_ec2_query(
            value["user_id_group_pairs"], pairs, f"{key_prefix}Groups"
        )


def deserialize_ec2_query(el: Element) -> StaleIpPermission:
    out: StaleIpPermission = {}  # type: ignore[typeddict-item]
    child_from_port = el.find("fromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_ip_protocol = el.find("ipProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_ip_ranges = el.find("ipRanges")
    if child_ip_ranges is not None:
        import capo_ec2.types.ip_ranges

        out["ip_ranges"] = capo_ec2.types.ip_ranges.deserialize_ec2_query(
            child_ip_ranges
        )
    child_prefix_list_ids = el.find("prefixListIds")
    if child_prefix_list_ids is not None:
        import capo_ec2.types.prefix_list_id_set

        out["prefix_list_ids"] = (
            capo_ec2.types.prefix_list_id_set.deserialize_ec2_query(
                child_prefix_list_ids
            )
        )
    child_to_port = el.find("toPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_user_id_group_pairs = el.find("groups")
    if child_user_id_group_pairs is not None:
        import capo_ec2.types.user_id_group_pair_set

        out["user_id_group_pairs"] = (
            capo_ec2.types.user_id_group_pair_set.deserialize_ec2_query(
                child_user_id_group_pairs
            )
        )
    return out
