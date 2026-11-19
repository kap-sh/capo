"""Generated from Smithy shape ``com.amazonaws.appstream#ImageSharedWithOthers``."""

from typing import Literal, TypeAlias, cast

ImageSharedWithOthers: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSharedWithOthers) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSharedWithOthers:
    return cast(ImageSharedWithOthers, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageSharedWithOthers) -> str:
    return value


def deserialize_cbor(data: str) -> ImageSharedWithOthers:
    return cast(ImageSharedWithOthers, data)
