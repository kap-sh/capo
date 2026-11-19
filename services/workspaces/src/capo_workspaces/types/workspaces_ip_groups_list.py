"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesIpGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_ip_group

WorkspacesIpGroupsList: TypeAlias = list[
    "capo_workspaces.types.workspaces_ip_group.WorkspacesIpGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesIpGroupsList) -> list:
    import capo_workspaces.types.workspaces_ip_group

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspaces_ip_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesIpGroupsList:
    import capo_workspaces.types.workspaces_ip_group

    out: WorkspacesIpGroupsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspaces_ip_group.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesIpGroupsList) -> list:
    import capo_workspaces.types.workspaces_ip_group

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspaces_ip_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkspacesIpGroupsList:
    import capo_workspaces.types.workspaces_ip_group

    out: WorkspacesIpGroupsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.workspaces_ip_group.deserialize_cbor(item))
    return out
