"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeEgressOnlyInternetGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_egress_only_internet_gateways_max_results
    import capo_ec2.types.egress_only_internet_gateway_id_list
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeEgressOnlyInternetGatewaysRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    egress_only_internet_gateway_ids: NotRequired[
        "capo_ec2.types.egress_only_internet_gateway_id_list.EgressOnlyInternetGatewayIdList"
    ]
    """<p>The IDs of the egress-only internet gateways.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_egress_only_internet_gateways_max_results.DescribeEgressOnlyInternetGatewaysMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeEgressOnlyInternetGatewaysRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "egress_only_internet_gateway_ids" in value:
        import capo_ec2.types.egress_only_internet_gateway_id_list

        capo_ec2.types.egress_only_internet_gateway_id_list.serialize_ec2_query(
            value["egress_only_internet_gateway_ids"],
            pairs,
            f"{key_prefix}EgressOnlyInternetGatewayId",
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeEgressOnlyInternetGatewaysRequest:
    out: DescribeEgressOnlyInternetGatewaysRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_egress_only_internet_gateway_ids = el.find("EgressOnlyInternetGatewayId")
    if child_egress_only_internet_gateway_ids is not None:
        import capo_ec2.types.egress_only_internet_gateway_id_list

        out["egress_only_internet_gateway_ids"] = (
            capo_ec2.types.egress_only_internet_gateway_id_list.deserialize_ec2_query(
                child_egress_only_internet_gateway_ids
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
