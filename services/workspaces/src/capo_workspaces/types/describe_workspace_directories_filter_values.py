"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspace_directories_filter_value

DescribeWorkspaceDirectoriesFilterValues: TypeAlias = list[
    "capo_workspaces.types.describe_workspace_directories_filter_value.DescribeWorkspaceDirectoriesFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspaceDirectoriesFilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceDirectoriesFilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DescribeWorkspaceDirectoriesFilterValues:
    return [item for item in data if item is not None]
