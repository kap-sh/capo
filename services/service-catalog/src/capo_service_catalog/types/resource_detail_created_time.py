"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceDetailCreatedTime``."""

import datetime
from typing import TypeAlias

ResourceDetailCreatedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetailCreatedTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ResourceDetailCreatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceDetailCreatedTime) -> ResourceDetailCreatedTime:
    return value


def deserialize_cbor(data: ResourceDetailCreatedTime) -> ResourceDetailCreatedTime:
    return data
