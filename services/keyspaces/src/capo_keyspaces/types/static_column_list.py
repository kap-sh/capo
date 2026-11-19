"""Generated from Smithy shape ``com.amazonaws.keyspaces#StaticColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.static_column

StaticColumnList: TypeAlias = list["capo_keyspaces.types.static_column.StaticColumn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticColumnList) -> list:
    import capo_keyspaces.types.static_column

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.static_column.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> StaticColumnList:
    import capo_keyspaces.types.static_column

    out: StaticColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.static_column.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StaticColumnList) -> list:
    import capo_keyspaces.types.static_column

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.static_column.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StaticColumnList:
    import capo_keyspaces.types.static_column

    out: StaticColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.static_column.deserialize_cbor(item))
    return out
