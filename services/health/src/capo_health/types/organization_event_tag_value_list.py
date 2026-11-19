"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

OrganizationEventTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationEventTagValueList:
    return [item for item in data if item is not None]
