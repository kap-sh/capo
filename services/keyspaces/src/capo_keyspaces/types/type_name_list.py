"""Generated from Smithy shape ``com.amazonaws.keyspaces#TypeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.type_name

TypeNameList: TypeAlias = list["capo_keyspaces.types.type_name.TypeName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TypeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TypeNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TypeNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TypeNameList:
    return [item for item in data if item is not None]
