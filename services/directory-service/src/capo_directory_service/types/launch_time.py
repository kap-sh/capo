"""Generated from Smithy shape ``com.amazonaws.directoryservice#LaunchTime``."""

import datetime
from typing import TypeAlias

LaunchTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LaunchTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LaunchTime) -> LaunchTime:
    return value


def deserialize_cbor(data: LaunchTime) -> LaunchTime:
    return data
