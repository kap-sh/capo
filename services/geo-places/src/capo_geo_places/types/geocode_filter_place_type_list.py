"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.geocode_filter_place_type

GeocodeFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.geocode_filter_place_type.GeocodeFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeFilterPlaceTypeList) -> list:
    import capo_geo_places.types.geocode_filter_place_type

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.geocode_filter_place_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeocodeFilterPlaceTypeList:
    import capo_geo_places.types.geocode_filter_place_type

    out: GeocodeFilterPlaceTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.geocode_filter_place_type.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GeocodeFilterPlaceTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
