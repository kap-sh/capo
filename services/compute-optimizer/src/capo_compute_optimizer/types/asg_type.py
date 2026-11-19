"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AsgType``."""

from typing import Literal, TypeAlias, cast

AsgType: TypeAlias = Literal[
    "SingleInstanceType",
    "MixedInstanceTypes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AsgType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AsgType:
    return cast(AsgType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AsgType) -> str:
    return value


def deserialize_cbor(data: str) -> AsgType:
    return cast(AsgType, data)
