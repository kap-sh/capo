"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.acl_name

ACLNameList: TypeAlias = list["capo_memorydb.types.acl_name.ACLName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ACLNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ACLNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ACLNameList:
    return [item for item in data if item is not None]
