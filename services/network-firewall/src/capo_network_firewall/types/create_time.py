"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateTime``."""

import datetime
from typing import TypeAlias

CreateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> CreateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateTime) -> CreateTime:
    return value


def deserialize_cbor(data: CreateTime) -> CreateTime:
    return data
