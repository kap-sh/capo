"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterLevelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.hierarchy_filter_level

HierarchyFilterLevelList: TypeAlias = list[
    "capo_quicksight.types.hierarchy_filter_level.HierarchyFilterLevel"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterLevelList) -> list:
    import capo_quicksight.types.hierarchy_filter_level

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.hierarchy_filter_level.serialize_json(item))
    return out


def deserialize_json(data: list) -> HierarchyFilterLevelList:
    import capo_quicksight.types.hierarchy_filter_level

    out: HierarchyFilterLevelList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.hierarchy_filter_level.deserialize_json(item))
    return out
