"""Generated from Smithy shape ``com.amazonaws.appstream#PackagingType``."""

from typing import Literal, TypeAlias, cast

PackagingType: TypeAlias = Literal[
    "CUSTOM",
    "APPSTREAM2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PackagingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PackagingType:
    return cast(PackagingType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PackagingType) -> str:
    return value


def deserialize_cbor(data: str) -> PackagingType:
    return cast(PackagingType, data)
