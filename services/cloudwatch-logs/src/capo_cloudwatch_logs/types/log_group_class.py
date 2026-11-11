"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupClass``."""

from typing import Literal, TypeAlias, cast

LogGroupClass: TypeAlias = Literal[
    "STANDARD",
    "INFREQUENT_ACCESS",
    "DELIVERY",
    "ESSENTIALS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogGroupClass:
    return cast(LogGroupClass, data)
