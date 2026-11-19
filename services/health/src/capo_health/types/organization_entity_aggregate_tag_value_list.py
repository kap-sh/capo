"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAggregateTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

OrganizationEntityAggregateTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAggregateTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationEntityAggregateTagValueList:
    return [item for item in data if item is not None]
