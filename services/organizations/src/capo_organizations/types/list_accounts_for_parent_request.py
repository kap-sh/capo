"""Generated from Smithy shape ``com.amazonaws.organizations#ListAccountsForParentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token
    import capo_organizations.types.parent_id


class ListAccountsForParentRequest(TypedDict, closed=True):
    parent_id: "capo_organizations.types.parent_id.ParentId"
    """<p>The unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountsForParentRequest) -> dict:
    out: dict = {}
    out["ParentId"] = value["parent_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountsForParentRequest:
    out: ListAccountsForParentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    else:
        out["parent_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
