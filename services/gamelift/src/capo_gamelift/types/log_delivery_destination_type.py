"""Generated from Smithy shape ``com.amazonaws.gamelift#LogDeliveryDestinationType``."""

from typing import Literal, TypeAlias, cast

LogDeliveryDestinationType: TypeAlias = Literal[
    "CLOUDWATCH",
    "S3",
    "FIREHOSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDeliveryDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogDeliveryDestinationType:
    return cast(LogDeliveryDestinationType, data)
