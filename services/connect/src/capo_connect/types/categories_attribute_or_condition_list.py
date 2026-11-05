"""Generated from Smithy shape ``com.amazonaws.connect#CategoriesAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.categories_attribute_and_condition

CategoriesAttributeOrConditionList: TypeAlias = list[
    "capo_connect.types.categories_attribute_and_condition.CategoriesAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoriesAttributeOrConditionList) -> list:
    import capo_connect.types.categories_attribute_and_condition

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.categories_attribute_and_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CategoriesAttributeOrConditionList:
    import capo_connect.types.categories_attribute_and_condition

    out: CategoriesAttributeOrConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.categories_attribute_and_condition.deserialize_json(item)
        )
    return out
