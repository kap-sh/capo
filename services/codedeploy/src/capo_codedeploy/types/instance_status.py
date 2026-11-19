"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

InstanceStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "Skipped",
    "Unknown",
    "Ready",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    return cast(InstanceStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceStatus:
    return cast(InstanceStatus, data)
