"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventsTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

DescribeEventsTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeEventsTagValueList:
    return [item for item in data if item is not None]
