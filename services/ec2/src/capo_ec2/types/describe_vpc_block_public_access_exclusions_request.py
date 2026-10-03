"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessExclusionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_vpc_block_public_access_exclusions_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string
    import capo_ec2.types.vpc_block_public_access_exclusion_id_list


class DescribeVpcBlockPublicAccessExclusionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>Filters for the request:</p> <ul> <li> <p> <code>resource-arn</code> - The Amazon Resource Name (ARN) of a exclusion.</p> </li> <li> <p> <code>internet-gateway-exclusion-mode</code> - The mode of a VPC BPA exclusion. Possible values: <code>allow-bidirectional | allow-egress</code>.</p> </li> <li> <p> <code>state</code> - The state of VPC BPA. Possible values: <code>create-in-progress | create-complete | update-in-progress | update-complete | delete-in-progress | deleted-complete | disable-in-progress | disable-complete</code> </p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>tag-value</code>: The value of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific value, regardless of the tag key.</p> </li> </ul>"""
    exclusion_ids: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusion_id_list.VpcBlockPublicAccessExclusionIdList"
    ]
    """<p>IDs of exclusions.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_vpc_block_public_access_exclusions_max_results.DescribeVpcBlockPublicAccessExclusionsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcBlockPublicAccessExclusionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "exclusion_ids" in value:
        import capo_ec2.types.vpc_block_public_access_exclusion_id_list

        capo_ec2.types.vpc_block_public_access_exclusion_id_list.serialize_ec2_query(
            value["exclusion_ids"], pairs, f"{key_prefix}ExclusionId"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcBlockPublicAccessExclusionsRequest:
    out: DescribeVpcBlockPublicAccessExclusionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_exclusion_ids = el.find("ExclusionId")
    if child_exclusion_ids is not None:
        import capo_ec2.types.vpc_block_public_access_exclusion_id_list

        out["exclusion_ids"] = (
            capo_ec2.types.vpc_block_public_access_exclusion_id_list.deserialize_ec2_query(
                child_exclusion_ids
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
