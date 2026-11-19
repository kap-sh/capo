"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityType``."""

from typing import Literal, TypeAlias, cast

PriorityType: TypeAlias = Literal[
    "LATENCY",
    "COST",
    "DESTINATION",
    "LOCATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PriorityType:
    return cast(PriorityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PriorityType) -> str:
    return value


def deserialize_cbor(data: str) -> PriorityType:
    return cast(PriorityType, data)
