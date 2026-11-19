"""Generated from Smithy shape ``com.amazonaws.datasync#ScheduleStatus``."""

from typing import Literal, TypeAlias, cast

ScheduleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleStatus:
    return cast(ScheduleStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScheduleStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ScheduleStatus:
    return cast(ScheduleStatus, data)
