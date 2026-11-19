"""Generated from Smithy shape ``com.amazonaws.acmpca#TStamp``."""

import datetime
from typing import TypeAlias

TStamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TStamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> TStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TStamp) -> TStamp:
    return value


def deserialize_cbor(data: TStamp) -> TStamp:
    return data
