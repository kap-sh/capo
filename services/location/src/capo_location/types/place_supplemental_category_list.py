"""Generated from Smithy shape ``com.amazonaws.location#PlaceSupplementalCategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.place_supplemental_category

PlaceSupplementalCategoryList: TypeAlias = list[
    "capo_location.types.place_supplemental_category.PlaceSupplementalCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceSupplementalCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaceSupplementalCategoryList:
    return [item for item in data if item is not None]


def redact_sensitive(value: PlaceSupplementalCategoryList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
