"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_filter

TagFilterList: TypeAlias = list["capo_observabilityadmin.types.tag_filter.TagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: TagFilterList) -> list:
    import capo_observabilityadmin.types.tag_filter

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.tag_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagFilterList:
    import capo_observabilityadmin.types.tag_filter

    out: TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_observabilityadmin.types.tag_filter.deserialize_json(item))
    return out
