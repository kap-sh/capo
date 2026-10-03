"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSubnetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_subnets_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id_string_list


class DescribeSubnetsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone for the subnet. You can also use <code>availabilityZone</code> as the filter name.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone for the subnet. You can also use <code>availabilityZoneId</code> as the filter name.</p> </li> <li> <p> <code>available-ip-address-count</code> - The number of IPv4 addresses in the subnet that are available.</p> </li> <li> <p> <code>cidr-block</code> - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet's CIDR block for information to be returned for the subnet. You can also use <code>cidr</code> or <code>cidrBlock</code> as the filter names.</p> </li> <li> <p> <code>customer-owned-ipv4-pool</code> - The customer-owned IPv4 address pool associated with the subnet.</p> </li> <li> <p> <code>default-for-az</code> - Indicates whether this is the default subnet for the Availability Zone (<code>true</code> | <code>false</code>). You can also use <code>defaultForAz</code> as the filter name.</p> </li> <li> <p> <code>enable-dns64</code> - Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.</p> </li> <li> <p> <code>enable-lni-at-device-index</code> - Indicates the device position for local network interfaces in this subnet. For example, <code>1</code> indicates local network interfaces in this subnet are the secondary network interface (eth1). </p> </li> <li> <p> <code>ipv6-cidr-block-association.ipv6-cidr-block</code> - An IPv6 CIDR block associated with the subnet.</p> </li> <li> <p> <code>ipv6-cidr-block-association.association-id</code> - An association ID for an IPv6 CIDR block associated with the subnet.</p> </li> <li> <p> <code>ipv6-cidr-block-association.state</code> - The state of an IPv6 CIDR block associated with the subnet.</p> </li> <li> <p> <code>ipv6-native</code> - Indicates whether this is an IPv6 only subnet (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>map-customer-owned-ip-on-launch</code> - Indicates whether a network interface created in this subnet (including a network interface created by <a>RunInstances</a>) receives a customer-owned IPv4 address.</p> </li> <li> <p> <code>map-public-ip-on-launch</code> - Indicates whether instances launched in this subnet receive a public IPv4 address.</p> </li> <li> <p> <code>outpost-arn</code> - The Amazon Resource Name (ARN) of the Outpost.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the subnet.</p> </li> <li> <p> <code>private-dns-name-options-on-launch.hostname-type</code> - The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name).</p> </li> <li> <p> <code>private-dns-name-options-on-launch.enable-resource-name-dns-a-record</code> - Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p> </li> <li> <p> <code>private-dns-name-options-on-launch.enable-resource-name-dns-aaaa-record</code> - Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p> </li> <li> <p> <code>state</code> - The state of the subnet (<code>pending</code> | <code>available</code>).</p> </li> <li> <p> <code>subnet-arn</code> - The Amazon Resource Name (ARN) of the subnet.</p> </li> <li> <p> <code>subnet-id</code> - The ID of the subnet.</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC for the subnet.</p> </li> </ul>"""
    subnet_ids: NotRequired["capo_ec2.types.subnet_id_string_list.SubnetIdStringList"]
    """<p>The IDs of the subnets.</p> <p>Default: Describes all your subnets.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_subnets_max_results.DescribeSubnetsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSubnetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "subnet_ids" in value:
        import capo_ec2.types.subnet_id_string_list

        capo_ec2.types.subnet_id_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetId"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeSubnetsRequest:
    out: DescribeSubnetsRequest = {}  # type: ignore[typeddict-item]
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_subnet_ids = el.find("SubnetId")
    if child_subnet_ids is not None:
        import capo_ec2.types.subnet_id_string_list

        out["subnet_ids"] = capo_ec2.types.subnet_id_string_list.deserialize_ec2_query(
            child_subnet_ids
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
    return out
