"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetStatus``."""

from typing import Literal, TypeAlias, cast

TargetStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "Skipped",
    "Unknown",
    "Ready",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetStatus:
    return cast(TargetStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetStatus) -> str:
    return value


def deserialize_cbor(data: str) -> TargetStatus:
    return cast(TargetStatus, data)
