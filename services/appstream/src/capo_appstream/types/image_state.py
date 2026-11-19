"""Generated from Smithy shape ``com.amazonaws.appstream#ImageState``."""

from typing import Literal, TypeAlias, cast

ImageState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "FAILED",
    "COPYING",
    "DELETING",
    "CREATING",
    "IMPORTING",
    "VALIDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageState:
    return cast(ImageState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageState) -> str:
    return value


def deserialize_cbor(data: str) -> ImageState:
    return cast(ImageState, data)
