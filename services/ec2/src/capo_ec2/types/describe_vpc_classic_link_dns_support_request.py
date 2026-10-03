"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkDnsSupportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_vpc_classic_link_dns_support_max_results
    import capo_ec2.types.describe_vpc_classic_link_dns_support_next_token
    import capo_ec2.types.vpc_classic_link_id_list


class DescribeVpcClassicLinkDnsSupportRequest(TypedDict, closed=True):
    vpc_ids: NotRequired["capo_ec2.types.vpc_classic_link_id_list.VpcClassicLinkIdList"]
    """<p>The IDs of the VPCs.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_vpc_classic_link_dns_support_max_results.DescribeVpcClassicLinkDnsSupportMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired[
        "capo_ec2.types.describe_vpc_classic_link_dns_support_next_token.DescribeVpcClassicLinkDnsSupportNextToken"
    ]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkDnsSupportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_ids" in value:
        import capo_ec2.types.vpc_classic_link_id_list

        capo_ec2.types.vpc_classic_link_id_list.serialize_ec2_query(
            value["vpc_ids"], pairs, f"{key_prefix}VpcIds"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkDnsSupportRequest:
    out: DescribeVpcClassicLinkDnsSupportRequest = {}  # type: ignore[typeddict-item]
    child_vpc_ids = el.find("VpcIds")
    if child_vpc_ids is not None:
        import capo_ec2.types.vpc_classic_link_id_list

        out["vpc_ids"] = capo_ec2.types.vpc_classic_link_id_list.deserialize_ec2_query(
            child_vpc_ids
        )
    child_max_results = el.find("maxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
