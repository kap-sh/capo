"""Generated from Smithy shape ``com.amazonaws.memorydb#SubnetIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.string

SubnetIdentifierList: TypeAlias = list["capo_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdentifierList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetIdentifierList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SubnetIdentifierList:
    return [item for item in data if item is not None]
