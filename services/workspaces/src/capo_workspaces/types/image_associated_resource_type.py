"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

ImageAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageAssociatedResourceType:
    return cast(ImageAssociatedResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageAssociatedResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> ImageAssociatedResourceType:
    return cast(ImageAssociatedResourceType, data)
