"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StepType``."""

from typing import Literal, TypeAlias, cast

StepType: TypeAlias = Literal[
    "CreateEbsSnapshot",
    "DeleteEbsVolume",
    "ModifyEbsVolume",
    "CreateEbsVolume",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StepType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StepType:
    return cast(StepType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StepType) -> str:
    return value


def deserialize_cbor(data: str) -> StepType:
    return cast(StepType, data)
