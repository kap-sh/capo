"""Generated from Smithy shape ``com.amazonaws.codedeploy#LifecycleEventStatus``."""

from typing import Literal, TypeAlias, cast

LifecycleEventStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "Skipped",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleEventStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleEventStatus:
    return cast(LifecycleEventStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LifecycleEventStatus) -> str:
    return value


def deserialize_cbor(data: str) -> LifecycleEventStatus:
    return cast(LifecycleEventStatus, data)
