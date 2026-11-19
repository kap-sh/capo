"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevisionType``."""

from typing import Literal, TypeAlias, cast

SourceRevisionType: TypeAlias = Literal[
    "COMMIT_ID",
    "IMAGE_DIGEST",
    "S3_OBJECT_VERSION_ID",
    "S3_OBJECT_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevisionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceRevisionType:
    return cast(SourceRevisionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceRevisionType) -> str:
    return value


def deserialize_cbor(data: str) -> SourceRevisionType:
    return cast(SourceRevisionType, data)
