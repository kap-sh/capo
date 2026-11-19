"""Generated from Smithy shape ``com.amazonaws.directconnect#ConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.connection

ConnectionList: TypeAlias = list["capo_direct_connect.types.connection.Connection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionList) -> list:
    import capo_direct_connect.types.connection

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.connection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionList:
    import capo_direct_connect.types.connection

    out: ConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.connection.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionList) -> list:
    import capo_direct_connect.types.connection

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.connection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConnectionList:
    import capo_direct_connect.types.connection

    out: ConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.connection.deserialize_cbor(item))
    return out
