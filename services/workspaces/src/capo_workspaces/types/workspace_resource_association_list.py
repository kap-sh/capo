"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_resource_association

WorkspaceResourceAssociationList: TypeAlias = list[
    "capo_workspaces.types.workspace_resource_association.WorkspaceResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceResourceAssociationList) -> list:
    import capo_workspaces.types.workspace_resource_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspace_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceResourceAssociationList:
    import capo_workspaces.types.workspace_resource_association

    out: WorkspaceResourceAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspace_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceResourceAssociationList) -> list:
    import capo_workspaces.types.workspace_resource_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspace_resource_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> WorkspaceResourceAssociationList:
    import capo_workspaces.types.workspace_resource_association

    out: WorkspaceResourceAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.workspace_resource_association.deserialize_cbor(item)
        )
    return out
