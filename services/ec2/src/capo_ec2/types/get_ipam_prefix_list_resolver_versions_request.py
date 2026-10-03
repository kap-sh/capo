"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.ipam_prefix_list_resolver_id
    import capo_ec2.types.ipam_prefix_list_resolver_version_number_set
    import capo_ec2.types.next_token


class GetIpamPrefixListResolverVersionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver whose versions you want to retrieve.</p>"""
    ipam_prefix_list_resolver_versions: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_version_number_set.IpamPrefixListResolverVersionNumberSet"
    ]
    """<p>Specific version numbers to retrieve. If not specified, all versions are returned.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to limit the results.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverVersionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_prefix_list_resolver_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverId",
                str(value["ipam_prefix_list_resolver_id"]),
            )
        )
    if "ipam_prefix_list_resolver_versions" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_version_number_set

        capo_ec2.types.ipam_prefix_list_resolver_version_number_set.serialize_ec2_query(
            value["ipam_prefix_list_resolver_versions"],
            pairs,
            f"{key_prefix}IpamPrefixListResolverVersion",
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverVersionsRequest:
    out: GetIpamPrefixListResolverVersionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_prefix_list_resolver_id = el.find("IpamPrefixListResolverId")
    if child_ipam_prefix_list_resolver_id is not None:
        out["ipam_prefix_list_resolver_id"] = str(
            child_ipam_prefix_list_resolver_id.text or ""
        )
    child_ipam_prefix_list_resolver_versions = el.find("IpamPrefixListResolverVersion")
    if child_ipam_prefix_list_resolver_versions is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_version_number_set

        out["ipam_prefix_list_resolver_versions"] = (
            capo_ec2.types.ipam_prefix_list_resolver_version_number_set.deserialize_ec2_query(
                child_ipam_prefix_list_resolver_versions
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
