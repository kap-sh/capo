"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AllocationStrategy``."""

from typing import Literal, TypeAlias, cast

AllocationStrategy: TypeAlias = Literal[
    "Prioritized",
    "LowestPrice",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AllocationStrategy:
    return cast(AllocationStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AllocationStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> AllocationStrategy:
    return cast(AllocationStrategy, data)
