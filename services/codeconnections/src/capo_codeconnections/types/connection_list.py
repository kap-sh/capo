"""Generated from Smithy shape ``com.amazonaws.codeconnections#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.connection

ConnectionList: TypeAlias = list["capo_codeconnections.types.connection.Connection"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionList) -> list:
    import capo_codeconnections.types.connection

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.connection.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionList:
    import capo_codeconnections.types.connection

    out: ConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codeconnections.types.connection.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionList) -> list:
    import capo_codeconnections.types.connection

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.connection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConnectionList:
    import capo_codeconnections.types.connection

    out: ConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codeconnections.types.connection.deserialize_cbor(item))
    return out
