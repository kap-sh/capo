"""Generated from Smithy shape ``com.amazonaws.gamelift#ZeroCapacityStrategy``."""

from typing import Literal, TypeAlias, cast

ZeroCapacityStrategy: TypeAlias = Literal[
    "MANUAL",
    "SCALE_TO_AND_FROM_ZERO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeroCapacityStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ZeroCapacityStrategy:
    return cast(ZeroCapacityStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ZeroCapacityStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> ZeroCapacityStrategy:
    return cast(ZeroCapacityStrategy, data)
