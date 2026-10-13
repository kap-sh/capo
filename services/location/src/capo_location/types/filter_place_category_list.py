"""Generated from Smithy shape ``com.amazonaws.location#FilterPlaceCategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.place_category

FilterPlaceCategoryList: TypeAlias = list[
    "capo_location.types.place_category.PlaceCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterPlaceCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterPlaceCategoryList:
    return [item for item in data if item is not None]


def redact_sensitive(value: FilterPlaceCategoryList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
