"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryStage``."""

from typing import Literal, TypeAlias, cast

DirectoryStage: TypeAlias = Literal[
    "Requested",
    "Creating",
    "Created",
    "Active",
    "Inoperable",
    "Impaired",
    "Restoring",
    "RestoreFailed",
    "Deleting",
    "Deleted",
    "Failed",
    "Updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryStage:
    return cast(DirectoryStage, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryStage) -> str:
    return value


def deserialize_cbor(data: str) -> DirectoryStage:
    return cast(DirectoryStage, data)
