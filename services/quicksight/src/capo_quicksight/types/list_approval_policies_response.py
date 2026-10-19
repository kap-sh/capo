"""Generated from Smithy shape ``com.amazonaws.quicksight#ListApprovalPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.approval_policy_list
    import capo_quicksight.types.pagination_token


class ListApprovalPoliciesResponse(TypedDict, closed=True):
    policies: "capo_quicksight.types.approval_policy_list.ApprovalPolicyList"
    """<p>The list of approval policies.</p>"""
    next_token: NotRequired["capo_quicksight.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalPoliciesResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.approval_policy_list

    out["Policies"] = capo_quicksight.types.approval_policy_list.serialize_json(
        value["policies"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApprovalPoliciesResponse:
    out: ListApprovalPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policies") is not None:
        import capo_quicksight.types.approval_policy_list

        out["policies"] = capo_quicksight.types.approval_policy_list.deserialize_json(
            data["Policies"]
        )
    else:
        out["policies"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
