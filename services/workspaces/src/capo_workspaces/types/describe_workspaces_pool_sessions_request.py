"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.limit50
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspaces_pool_id
    import capo_workspaces.types.workspaces_pool_user_id


class DescribeWorkspacesPoolSessionsRequest(TypedDict, closed=True):
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""
    user_id: NotRequired[
        "capo_workspaces.types.workspaces_pool_user_id.WorkspacesPoolUserId"
    ]
    """<p>The identifier of the user.</p>"""
    limit: NotRequired["capo_workspaces.types.limit50.Limit50"]
    """<p>The maximum size of each page of results. The default value is 20 and the maximum value is 50.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolSessionsRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolSessionsRequest:
    out: DescribeWorkspacesPoolSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
