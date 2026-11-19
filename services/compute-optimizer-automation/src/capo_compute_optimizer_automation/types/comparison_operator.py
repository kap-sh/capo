"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoreCase",
    "StringNotEqualsIgnoreCase",
    "StringLike",
    "StringNotLike",
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
    "StringEqualsIfExists",
    "StringNotEqualsIfExists",
    "StringEqualsIgnoreCaseIfExists",
    "StringNotEqualsIgnoreCaseIfExists",
    "StringLikeIfExists",
    "StringNotLikeIfExists",
    "NumericEqualsIfExists",
    "NumericNotEqualsIfExists",
    "NumericLessThanIfExists",
    "NumericLessThanEqualsIfExists",
    "NumericGreaterThanIfExists",
    "NumericGreaterThanEqualsIfExists",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComparisonOperator) -> str:
    return value


def deserialize_cbor(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
