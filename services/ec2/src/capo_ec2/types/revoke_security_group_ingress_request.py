"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupIngressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ip_permission_list
    import capo_ec2.types.security_group_id
    import capo_ec2.types.security_group_name
    import capo_ec2.types.security_group_rule_id_list
    import capo_ec2.types.string


class RevokeSecurityGroupIngressRequest(TypedDict, closed=True):
    cidr_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR IP address range. You can't specify this parameter when specifying a source security group.</p>"""
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).</p>"""
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["capo_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    ip_permissions: NotRequired["capo_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The sets of IP permissions. You can't specify a source security group and a CIDR IP address range in the same set of permissions.</p>"""
    ip_protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a>). Use <code>-1</code> to specify all.</p>"""
    source_security_group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>[Default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. The source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.</p>"""
    source_security_group_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Not supported.</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes).</p>"""
    security_group_rule_ids: NotRequired[
        "capo_ec2.types.security_group_rule_id_list.SecurityGroupRuleIdList"
    ]
    """<p>The IDs of the security group rules.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RevokeSecurityGroupIngressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr_ip" in value:
        pairs.append((f"{key_prefix}CidrIp", str(value["cidr_ip"])))
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "ip_permissions" in value:
        import capo_ec2.types.ip_permission_list

        capo_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions"], pairs, f"{key_prefix}IpPermissions"
        )
    if "ip_protocol" in value:
        pairs.append((f"{key_prefix}IpProtocol", str(value["ip_protocol"])))
    if "source_security_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}SourceSecurityGroupName",
                str(value["source_security_group_name"]),
            )
        )
    if "source_security_group_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}SourceSecurityGroupOwnerId",
                str(value["source_security_group_owner_id"]),
            )
        )
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))
    if "security_group_rule_ids" in value:
        import capo_ec2.types.security_group_rule_id_list

        capo_ec2.types.security_group_rule_id_list.serialize_ec2_query(
            value["security_group_rule_ids"], pairs, f"{key_prefix}SecurityGroupRuleId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> RevokeSecurityGroupIngressRequest:
    out: RevokeSecurityGroupIngressRequest = {}  # type: ignore[typeddict-item]
    child_cidr_ip = el.find("CidrIp")
    if child_cidr_ip is not None:
        out["cidr_ip"] = str(child_cidr_ip.text or "")
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_ip_permissions = el.find("IpPermissions")
    if child_ip_permissions is not None:
        import capo_ec2.types.ip_permission_list

        out["ip_permissions"] = capo_ec2.types.ip_permission_list.deserialize_ec2_query(
            child_ip_permissions
        )
    child_ip_protocol = el.find("IpProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_source_security_group_name = el.find("SourceSecurityGroupName")
    if child_source_security_group_name is not None:
        out["source_security_group_name"] = str(
            child_source_security_group_name.text or ""
        )
    child_source_security_group_owner_id = el.find("SourceSecurityGroupOwnerId")
    if child_source_security_group_owner_id is not None:
        out["source_security_group_owner_id"] = str(
            child_source_security_group_owner_id.text or ""
        )
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_security_group_rule_ids = el.find("SecurityGroupRuleId")
    if child_security_group_rule_ids is not None:
        import capo_ec2.types.security_group_rule_id_list

        out["security_group_rule_ids"] = (
            capo_ec2.types.security_group_rule_id_list.deserialize_ec2_query(
                child_security_group_rule_ids
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
