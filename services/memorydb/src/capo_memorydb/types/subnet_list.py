"""Generated from Smithy shape ``com.amazonaws.memorydb#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.subnet

SubnetList: TypeAlias = list["capo_memorydb.types.subnet.Subnet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetList) -> list:
    import capo_memorydb.types.subnet

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.subnet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubnetList:
    import capo_memorydb.types.subnet

    out: SubnetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.subnet.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetList) -> list:
    import capo_memorydb.types.subnet

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.subnet.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SubnetList:
    import capo_memorydb.types.subnet

    out: SubnetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.subnet.deserialize_cbor(item))
    return out
