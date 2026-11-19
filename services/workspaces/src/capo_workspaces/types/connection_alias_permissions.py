"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_permission

ConnectionAliasPermissions: TypeAlias = list[
    "capo_workspaces.types.connection_alias_permission.ConnectionAliasPermission"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasPermissions) -> list:
    import capo_workspaces.types.connection_alias_permission

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.connection_alias_permission.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasPermissions:
    import capo_workspaces.types.connection_alias_permission

    out: ConnectionAliasPermissions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connection_alias_permission.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasPermissions) -> list:
    import capo_workspaces.types.connection_alias_permission

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.connection_alias_permission.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ConnectionAliasPermissions:
    import capo_workspaces.types.connection_alias_permission

    out: ConnectionAliasPermissions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connection_alias_permission.deserialize_cbor(item)
        )
    return out
