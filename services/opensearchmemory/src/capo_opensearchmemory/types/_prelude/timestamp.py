"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: datetime.datetime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
