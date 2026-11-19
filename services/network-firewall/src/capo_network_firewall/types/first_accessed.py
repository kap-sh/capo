"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirstAccessed``."""

import datetime
from typing import TypeAlias

FirstAccessed: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirstAccessed) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> FirstAccessed:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirstAccessed) -> FirstAccessed:
    return value


def deserialize_cbor(data: FirstAccessed) -> FirstAccessed:
    return data
