"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_association

ConnectionAliasAssociationList: TypeAlias = list[
    "capo_workspaces.types.connection_alias_association.ConnectionAliasAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasAssociationList) -> list:
    import capo_workspaces.types.connection_alias_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.connection_alias_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasAssociationList:
    import capo_workspaces.types.connection_alias_association

    out: ConnectionAliasAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connection_alias_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasAssociationList) -> list:
    import capo_workspaces.types.connection_alias_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.connection_alias_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ConnectionAliasAssociationList:
    import capo_workspaces.types.connection_alias_association

    out: ConnectionAliasAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connection_alias_association.deserialize_cbor(item)
        )
    return out
