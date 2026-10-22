"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinationNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_name

DeliveryDestinationNames: TypeAlias = list[
    "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestinationNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeliveryDestinationNames:
    return [item for item in data if item is not None]
