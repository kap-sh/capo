"""Generated from Smithy shape ``com.amazonaws.datasync#ScheduleDisabledBy``."""

from typing import Literal, TypeAlias, cast

ScheduleDisabledBy: TypeAlias = Literal[
    "USER",
    "SERVICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleDisabledBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleDisabledBy:
    return cast(ScheduleDisabledBy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScheduleDisabledBy) -> str:
    return value


def deserialize_cbor(data: str) -> ScheduleDisabledBy:
    return cast(ScheduleDisabledBy, data)
