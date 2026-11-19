"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupAggregation``."""

from typing import Literal, TypeAlias, cast

ProtectionGroupAggregation: TypeAlias = Literal[
    "SUM",
    "MEAN",
    "MAX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupAggregation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionGroupAggregation:
    return cast(ProtectionGroupAggregation, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupAggregation) -> str:
    return value


def deserialize_cbor(data: str) -> ProtectionGroupAggregation:
    return cast(ProtectionGroupAggregation, data)
