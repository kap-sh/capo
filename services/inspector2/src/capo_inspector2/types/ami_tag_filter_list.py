"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiTagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.ami_tag_filter

AmiTagFilterList: TypeAlias = list["capo_inspector2.types.ami_tag_filter.AmiTagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: AmiTagFilterList) -> list:
    import capo_inspector2.types.ami_tag_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.ami_tag_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AmiTagFilterList:
    import capo_inspector2.types.ami_tag_filter

    out: AmiTagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_inspector2.types.ami_tag_filter.deserialize_json(item))
    return out
