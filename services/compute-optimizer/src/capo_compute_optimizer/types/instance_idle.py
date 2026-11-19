"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceIdle``."""

from typing import Literal, TypeAlias, cast

InstanceIdle: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceIdle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceIdle:
    return cast(InstanceIdle, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceIdle) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceIdle:
    return cast(InstanceIdle, data)
