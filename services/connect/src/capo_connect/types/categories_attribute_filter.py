"""Generated from Smithy shape ``com.amazonaws.connect#CategoriesAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.categories_attribute_and_condition
    import capo_connect.types.categories_attribute_or_condition_list
    import capo_connect.types.tag_condition


class CategoriesAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.categories_attribute_or_condition_list.CategoriesAttributeOrConditionList"
    ]
    """<p>A list of conditions that the filter evaluates using OR logic. A category segment matches when at least one of the conditions in the list is met.</p>"""
    and_condition: NotRequired[
        "capo_connect.types.categories_attribute_and_condition.CategoriesAttributeAndCondition"
    ]
    """<p>A condition that the filter evaluates using AND logic. A category segment matches only when all of the tag conditions in the condition are met.</p>"""
    tag_condition: NotRequired["capo_connect.types.tag_condition.TagCondition"]
    """<p>A single tag condition that a category segment must match. The category's rule must have the specified tag key and value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoriesAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.categories_attribute_or_condition_list

        out["OrConditions"] = (
            capo_connect.types.categories_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import capo_connect.types.categories_attribute_and_condition

        out["AndCondition"] = (
            capo_connect.types.categories_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import capo_connect.types.tag_condition

        out["TagCondition"] = capo_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    return out


def deserialize_json(data: dict) -> CategoriesAttributeFilter:
    out: CategoriesAttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("OrConditions") is not None:
        import capo_connect.types.categories_attribute_or_condition_list

        out["or_conditions"] = (
            capo_connect.types.categories_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if data.get("AndCondition") is not None:
        import capo_connect.types.categories_attribute_and_condition

        out["and_condition"] = (
            capo_connect.types.categories_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if data.get("TagCondition") is not None:
        import capo_connect.types.tag_condition

        out["tag_condition"] = capo_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    return out
