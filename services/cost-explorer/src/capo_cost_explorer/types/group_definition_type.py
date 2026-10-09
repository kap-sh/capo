"""Generated from Smithy shape ``com.amazonaws.costexplorer#GroupDefinitionType``."""

from typing import Literal, TypeAlias, cast

GroupDefinitionType: TypeAlias = Literal[
    "DIMENSION",
    "TAG",
    "COST_CATEGORY",
    "PRODUCT_ATTRIBUTE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupDefinitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupDefinitionType:
    return cast(GroupDefinitionType, data)
