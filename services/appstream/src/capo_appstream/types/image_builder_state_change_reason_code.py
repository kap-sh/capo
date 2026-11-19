"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

ImageBuilderStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "IMAGE_UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderStateChangeReasonCode:
    return cast(ImageBuilderStateChangeReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> ImageBuilderStateChangeReasonCode:
    return cast(ImageBuilderStateChangeReasonCode, data)
