"""Generated from Smithy shape ``com.amazonaws.memorydb#NetworkTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.network_type

NetworkTypeList: TypeAlias = list["capo_memorydb.types.network_type.NetworkType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkTypeList) -> list:
    import capo_memorydb.types.network_type

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.network_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkTypeList:
    import capo_memorydb.types.network_type

    out: NetworkTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.network_type.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkTypeList) -> list:
    import capo_memorydb.types.network_type

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.network_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NetworkTypeList:
    import capo_memorydb.types.network_type

    out: NetworkTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.network_type.deserialize_cbor(item))
    return out
