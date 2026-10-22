"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FilterResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn

FilterResourceArns: TypeAlias = list["capo_cloudwatch_logs.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterResourceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterResourceArns:
    return [item for item in data if item is not None]
