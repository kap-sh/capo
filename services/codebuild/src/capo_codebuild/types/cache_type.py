"""Generated from Smithy shape ``com.amazonaws.codebuild#CacheType``."""

from typing import Literal, TypeAlias, cast

CacheType: TypeAlias = Literal[
    "NO_CACHE",
    "S3",
    "LOCAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheType:
    return cast(CacheType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CacheType) -> str:
    return value


def deserialize_cbor(data: str) -> CacheType:
    return cast(CacheType, data)
