"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LastUpdateTime``."""

import datetime
from typing import TypeAlias

LastUpdateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastUpdateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastUpdateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastUpdateTime) -> LastUpdateTime:
    return value


def deserialize_cbor(data: LastUpdateTime) -> LastUpdateTime:
    return data
