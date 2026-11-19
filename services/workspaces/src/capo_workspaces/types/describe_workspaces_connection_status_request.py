"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesConnectionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_id_list


class DescribeWorkspacesConnectionStatusRequest(TypedDict, closed=True):
    workspace_ids: NotRequired[
        "capo_workspaces.types.workspace_id_list.WorkspaceIdList"
    ]
    """<p>The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesConnectionStatusRequest) -> dict:
    out: dict = {}
    if "workspace_ids" in value:
        import capo_workspaces.types.workspace_id_list

        out["WorkspaceIds"] = (
            capo_workspaces.types.workspace_id_list.serialize_aws_json_1_1(
                value["workspace_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesConnectionStatusRequest:
    out: DescribeWorkspacesConnectionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceIds") is not None:
        import capo_workspaces.types.workspace_id_list

        out["workspace_ids"] = (
            capo_workspaces.types.workspace_id_list.deserialize_aws_json_1_1(
                data["WorkspaceIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesConnectionStatusRequest) -> dict:
    out: dict = {}
    if "workspace_ids" in value:
        import capo_workspaces.types.workspace_id_list

        out["WorkspaceIds"] = capo_workspaces.types.workspace_id_list.serialize_cbor(
            value["workspace_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesConnectionStatusRequest:
    out: DescribeWorkspacesConnectionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceIds") is not None:
        import capo_workspaces.types.workspace_id_list

        out["workspace_ids"] = capo_workspaces.types.workspace_id_list.deserialize_cbor(
            data["WorkspaceIds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
