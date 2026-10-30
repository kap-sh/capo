"""Generated from Smithy shape ``com.amazonaws.opensearch#MetadataCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.metadata_category

MetadataCategoryList: TypeAlias = list[
    "capo_opensearch.types.metadata_category.MetadataCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> MetadataCategoryList:
    return [item for item in data if item is not None]
