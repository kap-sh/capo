"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Dimension``."""

from typing import Literal, TypeAlias, cast

Dimension: TypeAlias = Literal[
    "SavingsValue",
    "SavingsValueAfterDiscount",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    return cast(Dimension, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Dimension) -> str:
    return value


def deserialize_cbor(data: str) -> Dimension:
    return cast(Dimension, data)
