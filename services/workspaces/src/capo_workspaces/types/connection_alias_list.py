"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias

ConnectionAliasList: TypeAlias = list[
    "capo_workspaces.types.connection_alias.ConnectionAlias"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasList) -> list:
    import capo_workspaces.types.connection_alias

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.connection_alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasList:
    import capo_workspaces.types.connection_alias

    out: ConnectionAliasList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.connection_alias.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasList) -> list:
    import capo_workspaces.types.connection_alias

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.connection_alias.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConnectionAliasList:
    import capo_workspaces.types.connection_alias

    out: ConnectionAliasList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.connection_alias.deserialize_cbor(item))
    return out
