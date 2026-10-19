"""Generated from Smithy shape ``com.amazonaws.detective#ListMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn
    import capo_detective.types.member_results_limit
    import capo_detective.types.pagination_token


class ListMembersRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph for which to retrieve the list of member accounts.</p>"""
    next_token: NotRequired["capo_detective.types.pagination_token.PaginationToken"]
    """<p>For requests to retrieve the next page of member account results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.</p>"""
    max_results: NotRequired[
        "capo_detective.types.member_results_limit.MemberResultsLimit"
    ]
    """<p>The maximum number of member accounts to include in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListMembersRequest:
    out: ListMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
