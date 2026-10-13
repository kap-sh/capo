"""Generated from Smithy shape ``com.amazonaws.geoplaces#FoodTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.food_type

FoodTypeList: TypeAlias = list["capo_geo_places.types.food_type.FoodType"]


# --- restJson1 ser/de ---
def serialize_json(value: FoodTypeList) -> list:
    import capo_geo_places.types.food_type

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.food_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FoodTypeList:
    import capo_geo_places.types.food_type

    out: FoodTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.food_type.deserialize_json(item))
    return out


def redact_sensitive(value: FoodTypeList) -> list[Any]:
    import capo_geo_places.types.food_type

    return [capo_geo_places.types.food_type.redact_sensitive(item) for item in value]
