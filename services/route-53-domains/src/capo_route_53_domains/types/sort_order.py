"""Generated from Smithy shape ``com.amazonaws.route53domains#SortOrder``."""

from typing import Literal, TypeAlias, cast

SortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrder:
    return cast(SortOrder, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SortOrder) -> str:
    return value


def deserialize_cbor(data: str) -> SortOrder:
    return cast(SortOrder, data)
