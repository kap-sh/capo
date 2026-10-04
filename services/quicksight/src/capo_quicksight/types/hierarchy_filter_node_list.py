"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.hierarchy_filter_node

HierarchyFilterNodeList: TypeAlias = list[
    "capo_quicksight.types.hierarchy_filter_node.HierarchyFilterNode"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterNodeList) -> list:
    import capo_quicksight.types.hierarchy_filter_node

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.hierarchy_filter_node.serialize_json(item))
    return out


def deserialize_json(data: list) -> HierarchyFilterNodeList:
    import capo_quicksight.types.hierarchy_filter_node

    out: HierarchyFilterNodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.hierarchy_filter_node.deserialize_json(item))
    return out
