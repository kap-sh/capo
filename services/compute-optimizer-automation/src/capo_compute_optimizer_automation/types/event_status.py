"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EventStatus``."""

from typing import Literal, TypeAlias, cast

EventStatus: TypeAlias = Literal[
    "Ready",
    "InProgress",
    "Complete",
    "Failed",
    "Cancelled",
    "RollbackReady",
    "RollbackInProgress",
    "RollbackComplete",
    "RollbackFailed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventStatus:
    return cast(EventStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventStatus) -> str:
    return value


def deserialize_cbor(data: str) -> EventStatus:
    return cast(EventStatus, data)
