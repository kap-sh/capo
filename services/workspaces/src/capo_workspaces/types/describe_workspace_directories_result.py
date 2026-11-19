"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_list
    import capo_workspaces.types.pagination_token


class DescribeWorkspaceDirectoriesResult(TypedDict, closed=True):
    directories: NotRequired["capo_workspaces.types.directory_list.DirectoryList"]
    """<p>Information about the directories.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesResult) -> dict:
    out: dict = {}
    if "directories" in value:
        import capo_workspaces.types.directory_list

        out["Directories"] = (
            capo_workspaces.types.directory_list.serialize_aws_json_1_1(
                value["directories"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceDirectoriesResult:
    out: DescribeWorkspaceDirectoriesResult = {}  # type: ignore[typeddict-item]
    if data.get("Directories") is not None:
        import capo_workspaces.types.directory_list

        out["directories"] = (
            capo_workspaces.types.directory_list.deserialize_aws_json_1_1(
                data["Directories"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceDirectoriesResult) -> dict:
    out: dict = {}
    if "directories" in value:
        import capo_workspaces.types.directory_list

        out["Directories"] = capo_workspaces.types.directory_list.serialize_cbor(
            value["directories"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceDirectoriesResult:
    out: DescribeWorkspaceDirectoriesResult = {}  # type: ignore[typeddict-item]
    if data.get("Directories") is not None:
        import capo_workspaces.types.directory_list

        out["directories"] = capo_workspaces.types.directory_list.deserialize_cbor(
            data["Directories"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
