"""Generated from Smithy shape ``com.amazonaws.location#PlaceCategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.place_category

PlaceCategoryList: TypeAlias = list["capo_location.types.place_category.PlaceCategory"]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaceCategoryList:
    return [item for item in data if item is not None]


def redact_sensitive(value: PlaceCategoryList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
