"""Generated from Smithy shape ``com.amazonaws.codebuild#MachineType``."""

from typing import Literal, TypeAlias, cast

MachineType: TypeAlias = Literal[
    "GENERAL",
    "NVME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MachineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MachineType:
    return cast(MachineType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MachineType) -> str:
    return value


def deserialize_cbor(data: str) -> MachineType:
    return cast(MachineType, data)
