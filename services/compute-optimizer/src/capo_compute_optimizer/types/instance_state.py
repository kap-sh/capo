"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceState``."""

from typing import Literal, TypeAlias, cast

InstanceState: TypeAlias = Literal[
    "pending",
    "running",
    "shutting-down",
    "terminated",
    "stopping",
    "stopped",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceState:
    return cast(InstanceState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceState) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceState:
    return cast(InstanceState, data)
