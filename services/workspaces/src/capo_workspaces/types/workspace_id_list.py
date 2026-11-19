"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_id

WorkspaceIdList: TypeAlias = list["capo_workspaces.types.workspace_id.WorkspaceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspaceIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> WorkspaceIdList:
    return [item for item in data if item is not None]
