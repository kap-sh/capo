"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_request

WorkspaceRequestList: TypeAlias = list[
    "capo_workspaces.types.workspace_request.WorkspaceRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceRequestList) -> list:
    import capo_workspaces.types.workspace_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceRequestList:
    import capo_workspaces.types.workspace_request

    out: WorkspaceRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspace_request.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceRequestList) -> list:
    import capo_workspaces.types.workspace_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace_request.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkspaceRequestList:
    import capo_workspaces.types.workspace_request

    out: WorkspaceRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspace_request.deserialize_cbor(item))
    return out
