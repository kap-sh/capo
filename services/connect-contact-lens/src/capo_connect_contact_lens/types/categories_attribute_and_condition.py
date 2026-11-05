"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#CategoriesAttributeAndCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.tag_and_condition_list


class CategoriesAttributeAndCondition(TypedDict, closed=True):
    tag_conditions: NotRequired[
        "capo_connect_contact_lens.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A list of tag conditions. All of the tag conditions must be met for the condition to match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoriesAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import capo_connect_contact_lens.types.tag_and_condition_list

        out["TagConditions"] = (
            capo_connect_contact_lens.types.tag_and_condition_list.serialize_json(
                value["tag_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoriesAttributeAndCondition:
    out: CategoriesAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if data.get("TagConditions") is not None:
        import capo_connect_contact_lens.types.tag_and_condition_list

        out["tag_conditions"] = (
            capo_connect_contact_lens.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    return out
