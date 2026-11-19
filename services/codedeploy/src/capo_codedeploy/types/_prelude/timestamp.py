"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: datetime.datetime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: datetime.datetime) -> datetime.datetime:
    return value


def deserialize_cbor(data: datetime.datetime) -> datetime.datetime:
    return data
