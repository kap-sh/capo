"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddedDateTime``."""

import datetime
from typing import TypeAlias

AddedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddedDateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> AddedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AddedDateTime) -> AddedDateTime:
    return value


def deserialize_cbor(data: AddedDateTime) -> AddedDateTime:
    return data
