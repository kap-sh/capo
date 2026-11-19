"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id

ConnectionAliasIdList: TypeAlias = list[
    "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionAliasIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ConnectionAliasIdList:
    return [item for item in data if item is not None]
