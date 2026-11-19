"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LineTime``."""

import datetime
from typing import TypeAlias

LineTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LineTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LineTime) -> LineTime:
    return value


def deserialize_cbor(data: LineTime) -> LineTime:
    return data
