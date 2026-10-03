"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkAclsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_network_acls_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.network_acl_id_string_list
    import capo_ec2.types.string


class DescribeNetworkAclsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_network_acls_max_results.DescribeNetworkAclsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_acl_ids: NotRequired[
        "capo_ec2.types.network_acl_id_string_list.NetworkAclIdStringList"
    ]
    """<p>The IDs of the network ACLs.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>association.association-id</code> - The ID of an association ID for the ACL.</p> </li> <li> <p> <code>association.network-acl-id</code> - The ID of the network ACL involved in the association.</p> </li> <li> <p> <code>association.subnet-id</code> - The ID of the subnet involved in the association.</p> </li> <li> <p> <code>default</code> - Indicates whether the ACL is the default network ACL for the VPC.</p> </li> <li> <p> <code>entry.cidr</code> - The IPv4 CIDR range specified in the entry.</p> </li> <li> <p> <code>entry.icmp.code</code> - The ICMP code specified in the entry, if any.</p> </li> <li> <p> <code>entry.icmp.type</code> - The ICMP type specified in the entry, if any.</p> </li> <li> <p> <code>entry.ipv6-cidr</code> - The IPv6 CIDR range specified in the entry.</p> </li> <li> <p> <code>entry.port-range.from</code> - The start of the port range specified in the entry. </p> </li> <li> <p> <code>entry.port-range.to</code> - The end of the port range specified in the entry. </p> </li> <li> <p> <code>entry.protocol</code> - The protocol specified in the entry (<code>tcp</code> | <code>udp</code> | <code>icmp</code> or a protocol number).</p> </li> <li> <p> <code>entry.rule-action</code> - Allows or denies the matching traffic (<code>allow</code> | <code>deny</code>).</p> </li> <li> <p> <code>entry.egress</code> - A Boolean that indicates the type of rule. Specify <code>true</code> for egress rules, or <code>false</code> for ingress rules.</p> </li> <li> <p> <code>entry.rule-number</code> - The number of an entry (in other words, rule) in the set of ACL entries.</p> </li> <li> <p> <code>network-acl-id</code> - The ID of the network ACL.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the network ACL.</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC for the network ACL.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkAclsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "network_acl_ids" in value:
        import capo_ec2.types.network_acl_id_string_list

        capo_ec2.types.network_acl_id_string_list.serialize_ec2_query(
            value["network_acl_ids"], pairs, f"{key_prefix}NetworkAclId"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeNetworkAclsRequest:
    out: DescribeNetworkAclsRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_acl_ids = el.find("NetworkAclId")
    if child_network_acl_ids is not None:
        import capo_ec2.types.network_acl_id_string_list

        out["network_acl_ids"] = (
            capo_ec2.types.network_acl_id_string_list.deserialize_ec2_query(
                child_network_acl_ids
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
