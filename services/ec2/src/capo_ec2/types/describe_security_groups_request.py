"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_security_groups_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.group_id_string_list
    import capo_ec2.types.group_name_string_list
    import capo_ec2.types.string


class DescribeSecurityGroupsRequest(TypedDict, closed=True):
    group_ids: NotRequired["capo_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>The IDs of the security groups. Required for security groups in a nondefault VPC.</p> <p>Default: Describes all of your security groups.</p>"""
    group_names: NotRequired[
        "capo_ec2.types.group_name_string_list.GroupNameStringList"
    ]
    """<p>[Default VPC] The names of the security groups. You can specify either the security group name or the security group ID.</p> <p>Default: Describes all of your security groups.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_security_groups_max_results.DescribeSecurityGroupsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. This value can be between 5 and 1000. If this parameter is not specified, then all items are returned. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.</p> <ul> <li> <p> <code>description</code> - The description of the security group.</p> </li> <li> <p> <code>egress.ip-permission.cidr</code> - An IPv4 CIDR block for an outbound security group rule.</p> </li> <li> <p> <code>egress.ip-permission.from-port</code> - For an outbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number.</p> </li> <li> <p> <code>egress.ip-permission.group-id</code> - The ID of a security group that has been referenced in an outbound security group rule.</p> </li> <li> <p> <code>egress.ip-permission.group-name</code> - The name of a security group that is referenced in an outbound security group rule.</p> </li> <li> <p> <code>egress.ip-permission.ipv6-cidr</code> - An IPv6 CIDR block for an outbound security group rule.</p> </li> <li> <p> <code>egress.ip-permission.prefix-list-id</code> - The ID of a prefix list to which a security group rule allows outbound access.</p> </li> <li> <p> <code>egress.ip-permission.protocol</code> - The IP protocol for an outbound security group rule (<code>tcp</code> | <code>udp</code> | <code>icmp</code>, a protocol number, or -1 for all protocols).</p> </li> <li> <p> <code>egress.ip-permission.to-port</code> - For an outbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code.</p> </li> <li> <p> <code>egress.ip-permission.user-id</code> - The ID of an Amazon Web Services account that has been referenced in an outbound security group rule.</p> </li> <li> <p> <code>group-id</code> - The ID of the security group. </p> </li> <li> <p> <code>group-name</code> - The name of the security group.</p> </li> <li> <p> <code>ip-permission.cidr</code> - An IPv4 CIDR block for an inbound security group rule.</p> </li> <li> <p> <code>ip-permission.from-port</code> - For an inbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number.</p> </li> <li> <p> <code>ip-permission.group-id</code> - The ID of a security group that has been referenced in an inbound security group rule.</p> </li> <li> <p> <code>ip-permission.group-name</code> - The name of a security group that is referenced in an inbound security group rule.</p> </li> <li> <p> <code>ip-permission.ipv6-cidr</code> - An IPv6 CIDR block for an inbound security group rule.</p> </li> <li> <p> <code>ip-permission.prefix-list-id</code> - The ID of a prefix list from which a security group rule allows inbound access.</p> </li> <li> <p> <code>ip-permission.protocol</code> - The IP protocol for an inbound security group rule (<code>tcp</code> | <code>udp</code> | <code>icmp</code>, a protocol number, or -1 for all protocols).</p> </li> <li> <p> <code>ip-permission.to-port</code> - For an inbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code.</p> </li> <li> <p> <code>ip-permission.user-id</code> - The ID of an Amazon Web Services account that has been referenced in an inbound security group rule.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner of the security group.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC specified when the security group was created.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_ids" in value:
        import capo_ec2.types.group_id_string_list

        capo_ec2.types.group_id_string_list.serialize_ec2_query(
            value["group_ids"], pairs, f"{key_prefix}GroupId"
        )
    if "group_names" in value:
        import capo_ec2.types.group_name_string_list

        capo_ec2.types.group_name_string_list.serialize_ec2_query(
            value["group_names"], pairs, f"{key_prefix}GroupName"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupsRequest:
    out: DescribeSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
    child_group_ids = el.find("GroupId")
    if child_group_ids is not None:
        import capo_ec2.types.group_id_string_list

        out["group_ids"] = capo_ec2.types.group_id_string_list.deserialize_ec2_query(
            child_group_ids
        )
    child_group_names = el.find("GroupName")
    if child_group_names is not None:
        import capo_ec2.types.group_name_string_list

        out["group_names"] = (
            capo_ec2.types.group_name_string_list.deserialize_ec2_query(
                child_group_names
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
