"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesConnectionStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_connection_status_list


class DescribeWorkspacesConnectionStatusResult(TypedDict, closed=True):
    workspaces_connection_status: NotRequired[
        "capo_workspaces.types.workspace_connection_status_list.WorkspaceConnectionStatusList"
    ]
    """<p>Information about the connection status of the WorkSpace.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesConnectionStatusResult) -> dict:
    out: dict = {}
    if "workspaces_connection_status" in value:
        import capo_workspaces.types.workspace_connection_status_list

        out["WorkspacesConnectionStatus"] = (
            capo_workspaces.types.workspace_connection_status_list.serialize_aws_json_1_1(
                value["workspaces_connection_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesConnectionStatusResult:
    out: DescribeWorkspacesConnectionStatusResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesConnectionStatus") is not None:
        import capo_workspaces.types.workspace_connection_status_list

        out["workspaces_connection_status"] = (
            capo_workspaces.types.workspace_connection_status_list.deserialize_aws_json_1_1(
                data["WorkspacesConnectionStatus"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesConnectionStatusResult) -> dict:
    out: dict = {}
    if "workspaces_connection_status" in value:
        import capo_workspaces.types.workspace_connection_status_list

        out["WorkspacesConnectionStatus"] = (
            capo_workspaces.types.workspace_connection_status_list.serialize_cbor(
                value["workspaces_connection_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesConnectionStatusResult:
    out: DescribeWorkspacesConnectionStatusResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesConnectionStatus") is not None:
        import capo_workspaces.types.workspace_connection_status_list

        out["workspaces_connection_status"] = (
            capo_workspaces.types.workspace_connection_status_list.deserialize_cbor(
                data["WorkspacesConnectionStatus"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
