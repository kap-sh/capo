"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspace_directories_filter

DescribeWorkspaceDirectoriesFilterList: TypeAlias = list[
    "capo_workspaces.types.describe_workspace_directories_filter.DescribeWorkspaceDirectoriesFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilterList) -> list:
    import capo_workspaces.types.describe_workspace_directories_filter

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.describe_workspace_directories_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspaceDirectoriesFilterList:
    import capo_workspaces.types.describe_workspace_directories_filter

    out: DescribeWorkspaceDirectoriesFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.describe_workspace_directories_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceDirectoriesFilterList) -> list:
    import capo_workspaces.types.describe_workspace_directories_filter

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.describe_workspace_directories_filter.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> DescribeWorkspaceDirectoriesFilterList:
    import capo_workspaces.types.describe_workspace_directories_filter

    out: DescribeWorkspaceDirectoriesFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.describe_workspace_directories_filter.deserialize_cbor(
                item
            )
        )
    return out
