"""Generated from Smithy shape ``com.amazonaws.appstream#DirectoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.directory_name

DirectoryNameList: TypeAlias = list["capo_appstream.types.directory_name.DirectoryName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DirectoryNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DirectoryNameList:
    return [item for item in data if item is not None]
