"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.standby_workspace

StandbyWorkspacesList: TypeAlias = list[
    "capo_workspaces.types.standby_workspace.StandbyWorkspace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspacesList) -> list:
    import capo_workspaces.types.standby_workspace

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.standby_workspace.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StandbyWorkspacesList:
    import capo_workspaces.types.standby_workspace

    out: StandbyWorkspacesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.standby_workspace.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StandbyWorkspacesList) -> list:
    import capo_workspaces.types.standby_workspace

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.standby_workspace.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StandbyWorkspacesList:
    import capo_workspaces.types.standby_workspace

    out: StandbyWorkspacesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.standby_workspace.deserialize_cbor(item))
    return out
