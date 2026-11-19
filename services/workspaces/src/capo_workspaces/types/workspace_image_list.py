"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_image

WorkspaceImageList: TypeAlias = list[
    "capo_workspaces.types.workspace_image.WorkspaceImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageList) -> list:
    import capo_workspaces.types.workspace_image

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceImageList:
    import capo_workspaces.types.workspace_image

    out: WorkspaceImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspace_image.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceImageList) -> list:
    import capo_workspaces.types.workspace_image

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace_image.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkspaceImageList:
    import capo_workspaces.types.workspace_image

    out: WorkspaceImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspace_image.deserialize_cbor(item))
    return out
