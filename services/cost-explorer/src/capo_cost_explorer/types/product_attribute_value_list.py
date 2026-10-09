"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProductAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.value

ProductAttributeValueList: TypeAlias = list["capo_cost_explorer.types.value.Value"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductAttributeValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProductAttributeValueList:
    return [item for item in data if item is not None]
