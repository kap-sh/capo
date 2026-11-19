"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_image_id

WorkspaceImageIdList: TypeAlias = list[
    "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspaceImageIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceImageIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> WorkspaceImageIdList:
    return [item for item in data if item is not None]
