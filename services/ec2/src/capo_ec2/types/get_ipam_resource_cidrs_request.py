"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamResourceCidrsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipam_resource_type
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.next_token
    import capo_ec2.types.request_ipam_resource_tag
    import capo_ec2.types.string


class GetIpamResourceCidrsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the request. For more information about filtering, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html">Filtering CLI output</a>.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope that the resource is in.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool that the resource is in.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired["capo_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The resource type.</p>"""
    resource_tag: NotRequired[
        "capo_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
    ]
    """<p>The resource tag.</p>"""
    resource_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamResourceCidrsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{key_prefix}IpamScopeId", str(value["ipam_scope_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import capo_ec2.types.ipam_resource_type

        capo_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_tag" in value:
        import capo_ec2.types.request_ipam_resource_tag

        capo_ec2.types.request_ipam_resource_tag.serialize_ec2_query(
            value["resource_tag"], pairs, f"{key_prefix}ResourceTag"
        )
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))


def deserialize_ec2_query(el: Element) -> GetIpamResourceCidrsRequest:
    out: GetIpamResourceCidrsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_resource_type

        out["resource_type"] = capo_ec2.types.ipam_resource_type.deserialize_ec2_query(
            child_resource_type
        )
    child_resource_tag = el.find("ResourceTag")
    if child_resource_tag is not None:
        import capo_ec2.types.request_ipam_resource_tag

        out["resource_tag"] = (
            capo_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(
                child_resource_tag
            )
        )
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    return out
