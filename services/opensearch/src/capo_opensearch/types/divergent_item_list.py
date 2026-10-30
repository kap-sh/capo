"""Generated from Smithy shape ``com.amazonaws.opensearch#DivergentItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.divergent_item

DivergentItemList: TypeAlias = list[
    "capo_opensearch.types.divergent_item.DivergentItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DivergentItemList) -> list:
    import capo_opensearch.types.divergent_item

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.divergent_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DivergentItemList:
    import capo_opensearch.types.divergent_item

    out: DivergentItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearch.types.divergent_item.deserialize_json(item))
    return out
