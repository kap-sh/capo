"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageType``."""

from typing import Literal, TypeAlias, cast

ImageType: TypeAlias = Literal[
    "OWNED",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageType:
    return cast(ImageType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageType) -> str:
    return value


def deserialize_cbor(data: str) -> ImageType:
    return cast(ImageType, data)
