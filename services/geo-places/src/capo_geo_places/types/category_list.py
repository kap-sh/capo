"""Generated from Smithy shape ``com.amazonaws.geoplaces#CategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.category

CategoryList: TypeAlias = list["capo_geo_places.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryList) -> list:
    import capo_geo_places.types.category

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoryList:
    import capo_geo_places.types.category

    out: CategoryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.category.deserialize_json(item))
    return out


def redact_sensitive(value: CategoryList) -> list[Any]:
    import capo_geo_places.types.category

    return [capo_geo_places.types.category.redact_sensitive(item) for item in value]
