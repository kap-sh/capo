"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceConnectionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_connection_status

WorkspaceConnectionStatusList: TypeAlias = list[
    "capo_workspaces.types.workspace_connection_status.WorkspaceConnectionStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceConnectionStatusList) -> list:
    import capo_workspaces.types.workspace_connection_status

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspace_connection_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceConnectionStatusList:
    import capo_workspaces.types.workspace_connection_status

    out: WorkspaceConnectionStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspace_connection_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceConnectionStatusList) -> list:
    import capo_workspaces.types.workspace_connection_status

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspace_connection_status.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> WorkspaceConnectionStatusList:
    import capo_workspaces.types.workspace_connection_status

    out: WorkspaceConnectionStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspace_connection_status.deserialize_cbor(item)
        )
    return out
