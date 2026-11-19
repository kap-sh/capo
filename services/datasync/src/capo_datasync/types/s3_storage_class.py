"""Generated from Smithy shape ``com.amazonaws.datasync#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "GLACIER",
    "DEEP_ARCHIVE",
    "OUTPOSTS",
    "GLACIER_INSTANT_RETRIEVAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3StorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3StorageClass:
    return cast(S3StorageClass, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3StorageClass) -> str:
    return value


def deserialize_cbor(data: str) -> S3StorageClass:
    return cast(S3StorageClass, data)
