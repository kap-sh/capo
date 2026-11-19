"""Generated from Smithy shape ``com.amazonaws.codebuild#SortOrderType``."""

from typing import Literal, TypeAlias, cast

SortOrderType: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortOrderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrderType:
    return cast(SortOrderType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SortOrderType) -> str:
    return value


def deserialize_cbor(data: str) -> SortOrderType:
    return cast(SortOrderType, data)
