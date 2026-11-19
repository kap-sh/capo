"""Generated from Smithy shape ``com.amazonaws.keyspaces#ColumnDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.column_definition

ColumnDefinitionList: TypeAlias = list[
    "capo_keyspaces.types.column_definition.ColumnDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ColumnDefinitionList) -> list:
    import capo_keyspaces.types.column_definition

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.column_definition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ColumnDefinitionList:
    import capo_keyspaces.types.column_definition

    out: ColumnDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_keyspaces.types.column_definition.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ColumnDefinitionList) -> list:
    import capo_keyspaces.types.column_definition

    out: list = []
    for item in value:
        out.append(capo_keyspaces.types.column_definition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ColumnDefinitionList:
    import capo_keyspaces.types.column_definition

    out: ColumnDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_keyspaces.types.column_definition.deserialize_cbor(item))
    return out
