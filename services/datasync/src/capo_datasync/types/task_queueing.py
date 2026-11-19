"""Generated from Smithy shape ``com.amazonaws.datasync#TaskQueueing``."""

from typing import Literal, TypeAlias, cast

TaskQueueing: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskQueueing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskQueueing:
    return cast(TaskQueueing, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaskQueueing) -> str:
    return value


def deserialize_cbor(data: str) -> TaskQueueing:
    return cast(TaskQueueing, data)
