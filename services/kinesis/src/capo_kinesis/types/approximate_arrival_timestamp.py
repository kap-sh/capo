"""Generated from Smithy shape ``com.amazonaws.kinesis#ApproximateArrivalTimestamp``."""

import datetime
from typing import TypeAlias

ApproximateArrivalTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApproximateArrivalTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ApproximateArrivalTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
