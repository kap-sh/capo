"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_directory_name

WorkspaceDirectoryNameList: TypeAlias = list[
    "capo_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspaceDirectoryNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceDirectoryNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> WorkspaceDirectoryNameList:
    return [item for item in data if item is not None]
