"""Generated from Smithy shape ``com.amazonaws.appstream#ImageStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

ImageStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "IMAGE_BUILDER_NOT_AVAILABLE",
    "IMAGE_COPY_FAILURE",
    "IMAGE_UPDATE_FAILURE",
    "IMAGE_IMPORT_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStateChangeReasonCode:
    return cast(ImageStateChangeReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageStateChangeReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> ImageStateChangeReasonCode:
    return cast(ImageStateChangeReasonCode, data)
