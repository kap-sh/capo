"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SortOrder``."""

from typing import Literal, TypeAlias, cast

SortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SortOrder:
    return cast(SortOrder, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SortOrder) -> str:
    return value


def deserialize_cbor(data: str) -> SortOrder:
    return cast(SortOrder, data)
