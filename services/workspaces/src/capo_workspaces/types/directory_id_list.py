"""Generated from Smithy shape ``com.amazonaws.workspaces#DirectoryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id

DirectoryIdList: TypeAlias = list["capo_workspaces.types.directory_id.DirectoryId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DirectoryIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DirectoryIdList:
    return [item for item in data if item is not None]
