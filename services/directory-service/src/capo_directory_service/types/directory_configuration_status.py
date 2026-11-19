"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

DirectoryConfigurationStatus: TypeAlias = Literal[
    "Requested",
    "Updating",
    "Updated",
    "Failed",
    "Default",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryConfigurationStatus:
    return cast(DirectoryConfigurationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryConfigurationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DirectoryConfigurationStatus:
    return cast(DirectoryConfigurationStatus, data)
