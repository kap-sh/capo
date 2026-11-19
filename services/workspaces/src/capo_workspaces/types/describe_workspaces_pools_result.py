"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspaces_pools


class DescribeWorkspacesPoolsResult(TypedDict, closed=True):
    workspaces_pools: NotRequired[
        "capo_workspaces.types.workspaces_pools.WorkspacesPools"
    ]
    """<p>Information about the WorkSpaces Pools.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsResult) -> dict:
    out: dict = {}
    if "workspaces_pools" in value:
        import capo_workspaces.types.workspaces_pools

        out["WorkspacesPools"] = (
            capo_workspaces.types.workspaces_pools.serialize_aws_json_1_1(
                value["workspaces_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolsResult:
    out: DescribeWorkspacesPoolsResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesPools") is not None:
        import capo_workspaces.types.workspaces_pools

        out["workspaces_pools"] = (
            capo_workspaces.types.workspaces_pools.deserialize_aws_json_1_1(
                data["WorkspacesPools"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesPoolsResult) -> dict:
    out: dict = {}
    if "workspaces_pools" in value:
        import capo_workspaces.types.workspaces_pools

        out["WorkspacesPools"] = capo_workspaces.types.workspaces_pools.serialize_cbor(
            value["workspaces_pools"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesPoolsResult:
    out: DescribeWorkspacesPoolsResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesPools") is not None:
        import capo_workspaces.types.workspaces_pools

        out["workspaces_pools"] = (
            capo_workspaces.types.workspaces_pools.deserialize_cbor(
                data["WorkspacesPools"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
