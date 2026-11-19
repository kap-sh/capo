"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_list


class DescribeWorkspacesResult(TypedDict, closed=True):
    workspaces: NotRequired["capo_workspaces.types.workspace_list.WorkspaceList"]
    """<p>Information about the WorkSpaces.</p> <p>Because <a>CreateWorkspaces</a> is an asynchronous operation, some of the returned information could be incomplete.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesResult) -> dict:
    out: dict = {}
    if "workspaces" in value:
        import capo_workspaces.types.workspace_list

        out["Workspaces"] = capo_workspaces.types.workspace_list.serialize_aws_json_1_1(
            value["workspaces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesResult:
    out: DescribeWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("Workspaces") is not None:
        import capo_workspaces.types.workspace_list

        out["workspaces"] = (
            capo_workspaces.types.workspace_list.deserialize_aws_json_1_1(
                data["Workspaces"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesResult) -> dict:
    out: dict = {}
    if "workspaces" in value:
        import capo_workspaces.types.workspace_list

        out["Workspaces"] = capo_workspaces.types.workspace_list.serialize_cbor(
            value["workspaces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesResult:
    out: DescribeWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("Workspaces") is not None:
        import capo_workspaces.types.workspace_list

        out["workspaces"] = capo_workspaces.types.workspace_list.deserialize_cbor(
            data["Workspaces"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
