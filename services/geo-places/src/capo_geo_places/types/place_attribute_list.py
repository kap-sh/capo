"""Generated from Smithy shape ``com.amazonaws.geoplaces#PlaceAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.place_attribute

PlaceAttributeList: TypeAlias = list[
    "capo_geo_places.types.place_attribute.PlaceAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceAttributeList) -> list:
    import capo_geo_places.types.place_attribute

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.place_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlaceAttributeList:
    import capo_geo_places.types.place_attribute

    out: PlaceAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.place_attribute.deserialize_json(item))
    return out


def redact_sensitive(value: PlaceAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
