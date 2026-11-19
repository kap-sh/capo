"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AlarmCondition``."""

from typing import Literal, TypeAlias, cast

AlarmCondition: TypeAlias = Literal[
    "red",
    "green",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmCondition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmCondition:
    return cast(AlarmCondition, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmCondition) -> str:
    return value


def deserialize_cbor(data: str) -> AlarmCondition:
    return cast(AlarmCondition, data)
