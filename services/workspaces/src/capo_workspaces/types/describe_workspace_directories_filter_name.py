"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilterName``."""

from typing import Literal, TypeAlias, cast

DescribeWorkspaceDirectoriesFilterName: TypeAlias = Literal[
    "USER_IDENTITY_TYPE",
    "WORKSPACE_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspaceDirectoriesFilterName:
    return cast(DescribeWorkspaceDirectoriesFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceDirectoriesFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> DescribeWorkspaceDirectoriesFilterName:
    return cast(DescribeWorkspaceDirectoriesFilterName, data)
