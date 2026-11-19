"""Generated from Smithy shape ``com.amazonaws.memorydb#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.filter

FilterList: TypeAlias = list["capo_memorydb.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterList) -> list:
    import capo_memorydb.types.filter

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterList:
    import capo_memorydb.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterList) -> list:
    import capo_memorydb.types.filter

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterList:
    import capo_memorydb.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.filter.deserialize_cbor(item))
    return out
