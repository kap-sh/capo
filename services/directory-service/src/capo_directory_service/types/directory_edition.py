"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryEdition``."""

from typing import Literal, TypeAlias, cast

DirectoryEdition: TypeAlias = Literal[
    "Enterprise",
    "Standard",
    "Hybrid",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryEdition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryEdition:
    return cast(DirectoryEdition, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryEdition) -> str:
    return value


def deserialize_cbor(data: str) -> DirectoryEdition:
    return cast(DirectoryEdition, data)
