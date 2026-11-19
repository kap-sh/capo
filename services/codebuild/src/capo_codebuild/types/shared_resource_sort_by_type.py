"""Generated from Smithy shape ``com.amazonaws.codebuild#SharedResourceSortByType``."""

from typing import Literal, TypeAlias, cast

SharedResourceSortByType: TypeAlias = Literal[
    "ARN",
    "MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedResourceSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharedResourceSortByType:
    return cast(SharedResourceSortByType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SharedResourceSortByType) -> str:
    return value


def deserialize_cbor(data: str) -> SharedResourceSortByType:
    return cast(SharedResourceSortByType, data)
