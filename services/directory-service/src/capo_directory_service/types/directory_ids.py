"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id

DirectoryIds: TypeAlias = list["capo_directory_service.types.directory_id.DirectoryId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DirectoryIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DirectoryIds:
    return [item for item in data if item is not None]
