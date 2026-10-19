"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token


class DescribeConnectionAliasPermissionsRequest(TypedDict, closed=True):
    alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results. </p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasPermissionsRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasPermissionsRequest:
    out: DescribeConnectionAliasPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    else:
        out["alias_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
