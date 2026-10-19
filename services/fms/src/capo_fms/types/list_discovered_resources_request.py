"""Generated from Smithy shape ``com.amazonaws.fms#ListDiscoveredResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id_list
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token
    import capo_fms.types.resource_type


class ListDiscoveredResourcesRequest(TypedDict, closed=True):
    member_account_ids: "capo_fms.types.aws_account_id_list.AWSAccountIdList"
    """<p>The Amazon Web Services account IDs to discover resources in. Only one account is supported per request. The account must be a member of your organization.</p>"""
    resource_type: "capo_fms.types.resource_type.ResourceType"
    """<p>The type of resources to discover.</p>"""
    max_results: NotRequired[
        "capo_fms.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesRequest) -> dict:
    out: dict = {}
    import capo_fms.types.aws_account_id_list

    out["MemberAccountIds"] = capo_fms.types.aws_account_id_list.serialize_aws_json_1_1(
        value["member_account_ids"]
    )
    out["ResourceType"] = value["resource_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesRequest:
    out: ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MemberAccountIds") is not None:
        import capo_fms.types.aws_account_id_list

        out["member_account_ids"] = (
            capo_fms.types.aws_account_id_list.deserialize_aws_json_1_1(
                data["MemberAccountIds"]
            )
        )
    else:
        out["member_account_ids"] = []
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
