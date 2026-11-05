"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#TagAndConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.tag_condition

TagAndConditionList: TypeAlias = list[
    "capo_connect_contact_lens.types.tag_condition.TagCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagAndConditionList) -> list:
    import capo_connect_contact_lens.types.tag_condition

    out: list = []
    for item in value:
        out.append(capo_connect_contact_lens.types.tag_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagAndConditionList:
    import capo_connect_contact_lens.types.tag_condition

    out: TagAndConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect_contact_lens.types.tag_condition.deserialize_json(item))
    return out
