"""Generated from Smithy shape ``com.amazonaws.gamelift#ComparisonOperatorType``."""

from typing import Literal, TypeAlias, cast

ComparisonOperatorType: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperatorType:
    return cast(ComparisonOperatorType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComparisonOperatorType) -> str:
    return value


def deserialize_cbor(data: str) -> ComparisonOperatorType:
    return cast(ComparisonOperatorType, data)
