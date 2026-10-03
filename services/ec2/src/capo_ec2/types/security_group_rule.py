"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.referenced_security_group
    import capo_ec2.types.security_group_id
    import capo_ec2.types.security_group_rule_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SecurityGroupRule(TypedDict, closed=True):
    security_group_rule_id: NotRequired[
        "capo_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>The ID of the security group rule.</p>"""
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    group_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the security group. </p>"""
    is_egress: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the security group rule is an outbound rule.</p>"""
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a>). </p> <p>Use <code>-1</code> to specify all protocols.</p>"""
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p>"""
    cidr_ipv4: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR range.</p>"""
    cidr_ipv6: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR range.</p>"""
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    referenced_group_info: NotRequired[
        "capo_ec2.types.referenced_security_group.ReferencedSecurityGroup"
    ]
    """<p>Describes the security group that is referenced in the rule.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group rule description.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags applied to the security group rule.</p>"""
    security_group_rule_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "security_group_rule_id" in value:
        pairs.append(
            (f"{key_prefix}SecurityGroupRuleId", str(value["security_group_rule_id"]))
        )
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "group_owner_id" in value:
        pairs.append((f"{key_prefix}GroupOwnerId", str(value["group_owner_id"])))
    if "is_egress" in value:
        pairs.append(
            (f"{key_prefix}IsEgress", "true" if value["is_egress"] else "false")
        )
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
    if "referenced_group_info" in value:
        import capo_ec2.types.referenced_security_group

        capo_ec2.types.referenced_security_group.serialize_ec2_query(
            value["referenced_group_info"], pairs, f"{key_prefix}ReferencedGroupInfo"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "security_group_rule_arn" in value:
        pairs.append(
            (f"{key_prefix}SecurityGroupRuleArn", str(value["security_group_rule_arn"]))
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupRule:
    out: SecurityGroupRule = {}  # type: ignore[typeddict-item]
    child_security_group_rule_id = el.find("securityGroupRuleId")
    if child_security_group_rule_id is not None:
        out["security_group_rule_id"] = str(child_security_group_rule_id.text or "")
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_owner_id = el.find("groupOwnerId")
    if child_group_owner_id is not None:
        out["group_owner_id"] = str(child_group_owner_id.text or "")
    child_is_egress = el.find("isEgress")
    if child_is_egress is not None:
        out["is_egress"] = (child_is_egress.text or "").lower() == "true"
    child_ip_protocol = el.find("ipProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_from_port = el.find("fromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("toPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_cidr_ipv4 = el.find("cidrIpv4")
    if child_cidr_ipv4 is not None:
        out["cidr_ipv4"] = str(child_cidr_ipv4.text or "")
    child_cidr_ipv6 = el.find("cidrIpv6")
    if child_cidr_ipv6 is not None:
        out["cidr_ipv6"] = str(child_cidr_ipv6.text or "")
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_referenced_group_info = el.find("referencedGroupInfo")
    if child_referenced_group_info is not None:
        import capo_ec2.types.referenced_security_group

        out["referenced_group_info"] = (
            capo_ec2.types.referenced_security_group.deserialize_ec2_query(
                child_referenced_group_info
            )
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_security_group_rule_arn = el.find("securityGroupRuleArn")
    if child_security_group_rule_arn is not None:
        out["security_group_rule_arn"] = str(child_security_group_rule_arn.text or "")
    return out
