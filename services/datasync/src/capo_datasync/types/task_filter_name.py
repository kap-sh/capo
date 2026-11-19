"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilterName``."""

from typing import Literal, TypeAlias, cast

TaskFilterName: TypeAlias = Literal[
    "LocationId",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskFilterName:
    return cast(TaskFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaskFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> TaskFilterName:
    return cast(TaskFilterName, data)
