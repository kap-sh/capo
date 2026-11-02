"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupImpacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_impact

LogGroupImpacts: TypeAlias = list[
    "capo_cloudwatch_logs.types.log_group_impact.LogGroupImpact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupImpacts) -> list:
    import capo_cloudwatch_logs.types.log_group_impact

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.log_group_impact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogGroupImpacts:
    import capo_cloudwatch_logs.types.log_group_impact

    out: LogGroupImpacts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.log_group_impact.deserialize_aws_json_1_1(item)
        )
    return out
