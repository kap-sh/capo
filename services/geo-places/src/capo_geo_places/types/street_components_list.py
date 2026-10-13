"""Generated from Smithy shape ``com.amazonaws.geoplaces#StreetComponentsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.street_components

StreetComponentsList: TypeAlias = list[
    "capo_geo_places.types.street_components.StreetComponents"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreetComponentsList) -> list:
    import capo_geo_places.types.street_components

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.street_components.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreetComponentsList:
    import capo_geo_places.types.street_components

    out: StreetComponentsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.street_components.deserialize_json(item))
    return out


def redact_sensitive(value: StreetComponentsList) -> list[Any]:
    import capo_geo_places.types.street_components

    return [
        capo_geo_places.types.street_components.redact_sensitive(item) for item in value
    ]
