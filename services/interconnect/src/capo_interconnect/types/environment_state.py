"""Generated from Smithy shape ``com.amazonaws.interconnect#EnvironmentState``."""

from typing import Literal, TypeAlias, cast

EnvironmentState: TypeAlias = Literal[
    "available",
    "limited",
    "unavailable",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnvironmentState:
    return cast(EnvironmentState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentState) -> str:
    return value


def deserialize_cbor(data: str) -> EnvironmentState:
    return cast(EnvironmentState, data)
