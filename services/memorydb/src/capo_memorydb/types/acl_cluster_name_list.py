"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLClusterNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.string

ACLClusterNameList: TypeAlias = list["capo_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLClusterNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ACLClusterNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ACLClusterNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ACLClusterNameList:
    return [item for item in data if item is not None]
