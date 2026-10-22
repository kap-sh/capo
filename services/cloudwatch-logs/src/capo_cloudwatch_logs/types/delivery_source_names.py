"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source_name

DeliverySourceNames: TypeAlias = list[
    "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeliverySourceNames:
    return [item for item in data if item is not None]
